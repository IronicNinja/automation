from selenium import webdriver
from time import sleep
import random

rand_time = random.randint(10, 2000)
sleep(rand_time)

people_list = [[]]

class harinbot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(r'C:\Users\evanz\Desktop\allbots\chromedriver', options=chrome_options)

    def filled(self, firstname, lastname, emailname):
        self.driver.get('link name')

        sleep(3)
        fname = self.driver.find_element_by_xpath('//*[@id="first_3"]')
        fname.click()
        fname.send_keys(firstname)

        sleep(2)
        lname = self.driver.find_element_by_xpath('//*[@id="last_3"]')
        lname.click()
        lname.send_keys(lastname)

        sleep(4)
        email = self.driver.find_element_by_xpath('//*[@id="input_20"]')
        email.click()
        email.send_keys(emailname)

        sleep(1)
        symptoms = self.driver.find_element_by_xpath('//*[@id="label_input_15_1"]')
        symptoms.click()

        sleep(1)
        contact = self.driver.find_element_by_xpath('//*[@id="label_input_5_1"]')
        contact.click()

        submit = self.driver.find_element_by_xpath('//*[@id="input_2"]')
        submit.click()

bot = harinbot()
for name in people_list:
    bot.filled(name[0], name[1], name[2])
    sleep(random.randint(2, 20))
