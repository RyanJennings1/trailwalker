#!/usr/bin/env python3

import time
import os
import json
from selenium import webdriver

CHROME_DRIVER_FILEPATH = os.getenv("HOME") + "/.chromedriver/chromedriver"

def main():
    data = load_json()
    login_to_trailhead(data)


def load_json():
    json_data = open("config.json").read()
    return json.loads(json_data)

def login_to_trailhead(login_variables):
    driver = webdriver.Chrome(CHROME_DRIVER_FILEPATH)
    driver.get('https://trailhead.salesforce.com/en')
    time.sleep(2)

    login_button = driver.find_elements_by_xpath("//*[contains(text(), 'Login')]")[1]
    login_button.click()

    time.sleep(2)

    google_plus_button = driver.find_elements_by_xpath("//*[contains(text(), 'Log in with Google+')]")[0]
    google_plus_button.click()

    email_input = driver.find_element_by_tag_name('input')
    email_input.send_keys(login_variables['email'])

    next_button = driver.find_elements_by_xpath("//div[@role='button']")[0]
    next_button.click()

    time.sleep(2)

    phone_input = driver.find_element_by_id('recoveryIdentifierId')
    phone_input.send_keys(login_variables['phone_number'])

    next_button2 = driver.find_elements_by_xpath("//div[@role='button']")[0]
    next_button2.click()

    time.sleep(2)
    first_name_input = driver.find_element_by_id('firstName')
    first_name_input.send_keys(login_variables['first_name'])

    time.sleep(2)
    last_name_input = driver.find_element_by_id('lastName')
    last_name_input.send_keys(login_variables['last_name'])

    next_button3 = driver.find_elements_by_xpath("//div[@role='button']")[0]
    next_button3.click()

    time.sleep(2)
    send_text_button = driver.find_elements_by_xpath("//div[@role='button']")[0]
    send_text_button.click()

    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
