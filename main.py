#!/usr/bin/env python3

import time
import os
import json
from selenium import webdriver

CHROME_DRIVER_FILEPATH = os.getenv("HOME") + "/.chromedriver/chromedriver"

def main():
    # data = load_json()
    # login_to_trailhead(data)
    answers_data = read_answers()
    titles = get_trail_titles()
    NEWTITLE = set_title(titles, answers_data)
    print('new title')
    print(NEWTITLE)
    '''
    for i in range(len(titles)):
        if (has_trail_been_walked(titles[i], answers_data)) {
            NEWTITLE = titles[i]
            return 
        }
    NEWTITLE = titles[0]
    NEWTITLE = "my first trail"
    ANSWERS = {
        "1": "A",
        "2": "B",
        "3": "C"
    }
    a = write_answers(NEWTITLE, ANSWERS)
    '''
    # select_trail()

    if has_trail_been_walked(NEWTITLE, answers_data):
        print('walked ' + str(NEWTITLE))
    else:
        print('not walked ' + str(NEWTITLE))


def load_json():
    """
    Load config.json file and return json object of config data
    """
    json_data = open("config.json").read()
    return json.loads(json_data)

def login_to_trailhead(login_variables):
    """
    Login to trailhead
    """
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

    time.sleep(30)
    text_code_button = driver.find_elements_by_xpath("//div[@role='button']")[0]
    text_code_button.click()

    time.sleep(3)
    choose_account_button = driver.find_elements_by_xpath("//div[@role='button']")[0]
    choose_account_button.click()

    time.sleep(6)
    enter_password = driver.find_elements_by_xpath("//input[@type='password']")[0]
    enter_password.send_keys('PASSWORD HERE')

    time.sleep(5)
    password_next_button = driver.find_element_by_id("passwordNext")
    password_next_button.click()

    time.sleep(10000)
    driver.quit()

def get_trail_titles():
    """
    Navigate to trails page
    return array of trail titles on page
    """
    driver = webdriver.Chrome(CHROME_DRIVER_FILEPATH)
    driver.get('https://trailhead.salesforce.com/en/trails')

    time.sleep(3)
    return driver.find_elements_by_class_name('tile-title')

def select_trail(title):
    """
    Haven't wrote this function yet just copied get_trail_titles

    Function will go into trail given title
    """
    driver = webdriver.Chrome(CHROME_DRIVER_FILEPATH)
    driver.get('https://trailhead.salesforce.com/en/trails')

    time.sleep(3)
    titles = driver.find_elements_by_class_name('tile-title')
    # Check if first title has already been done
    driver.quit()

def set_title(titles, answers_data):
    """
    Need to change this

    Loop through title array
    if the title text is in answer.json then return the title
    else return the first title
    """
    for i in range(len(titles)):
        if has_trail_been_walked(titles[i].text, answers_data):
            return titles[i].text
    return titles[0].text

def has_trail_been_walked(title, answers_data):
    """
    return True if the title has already been put in the answer.json file
    return False if there is no answers for the title
    """
    return title in answers_data

def guess_answers():
    return False

def read_answers():
    """
    read data from answer.json and convert to json object
    """
    with open('answer.json') as f:
        return json.load(f)

def write_answers(title, answers):
    """
    Add dict of answers in answer.json file

    example:
    write_answers('security trail', { '1': 'a', '2': 'b' })
    """
    answer_data = read_answers()

    answer_data[title] = answers

    with open('answer.json', 'w') as f:
        json.dump(answer_data, f)
    return False

if __name__ == "__main__":
    main()
