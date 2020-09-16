### sends at 2PM

from discord_webhook import DiscordWebhook, DiscordEmbed
import pandas as pd
from datetime import date, datetime, timedelta

webhook = DiscordWebhook('https://discord.com/api/webhooks/737017721442533416/fn9KVJlGzTDulOhvNsjHViKFXDE03Wo6Y2-xzISnZjcGJ-YSJBCnHXBvDY3qNR4cujDV')

today = datetime.strptime(str(date.today()).replace(' 00:00:00', ''), "%Y-%m-%d")

df = pd.read_excel('ScholarshipDates.xlsx')

embed = DiscordEmbed(title='Scholarship Reminders', description='<@&706946244869619723>', color=242424)

change_rate = 12

def run(keyword, title):
    deadline_list = []
    unsure_list = []
    started_list = []
    ending_soon_list = []
    ended_list = []
    for row in range(len(df[keyword])):
        org = str(df[keyword][row])

        if org == 'NaT':
            unsure_list.append(df['Scholarship Name'][row])
            continue

        deadline_time = org.replace(' 00:00:00', '')
        deadline = datetime.strptime(deadline_time, "%Y-%m-%d")
        diff = deadline - today

        if "days" in str(diff):
            num = int(str(diff).replace(' days, 0:00:00', ''))
        else:
            num = int(str(diff).replace(' day, 0:00:00', ''))

        if keyword == 'Start':
            if num > 0:
                deadline_list.append([diff, df['Scholarship Name'][row]])
            else:
                started_list.append(df['Scholarship Name'][row])
        else:
            if num > change_rate:
                diff -= timedelta(days=change_rate)
                deadline_list.append([diff, df['Scholarship Name'][row]])
            elif num > 0 and change_rate >= num:
                ending_soon_list.append(df['Scholarship Name'][row])
            else:
                ended_list.append(df['Scholarship Name'][row])

    deadline_list.sort()        

    s = ''
    for ending_soon in ending_soon_list:
        s += (ending_soon + ': Ending Soon! \n')

    for deadline in deadline_list:
        days = str(deadline[0]).replace(', 0:00:00', '')
        s += (deadline[1] + ': ' + days + "\n")

    for unsure in unsure_list:
        s += (unsure + ': Unsure \n')

    for ended in ended_list:
        s += (ended + ': Ended \n')

    for started in started_list:
        s += (started + ': Started \n')

    embed.add_embed_field(name=title, value=s)
    
while True:
    try:
        run('Start', 'Starting Soon')
        run('End', 'Deadlines')
        webhook.add_embed(embed)
        break
    except (RuntimeError, TypeError, NameError, AssertionError, AttributeError, EOFError, FloatingPointError, GeneratorExit, 
        ImportError, IndexError, KeyError, KeyboardInterrupt, MemoryError, NotImplementedError, OSError, OverflowError, ReferenceError,
        StopIteration, SyntaxError, IndentationError, TabError, SystemError, SystemExit, UnboundLocalError, UnicodeError, UnicodeEncodeError,
        UnicodeDecodeError, UnicodeTranslateError, ZeroDivisionError, ValueError):
        embed1 = DiscordEmbed(title='THERE IS AN ERROR', description='<@&706946244869619723>', color=242424)
        webhook.add_embed(embed1)
        break

webhook.execute()