#!/usr/local/bin/python3
from selenium import webdriver
import time
import random


class SouthwestCheckIn:
    def __init__(self, confirmation_num, first_name, last_name, number):
        self.confirmation_num = confirmation_num
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.driver = webdriver.Chrome()
        self.check_in_link = 'https://www.southwest.com/air/check-in/index.html'

    def check_in(self):
        self.driver.get(self.check_in_link)
        conf_input = self.driver.find_element_by_id('confirmationNumber')
        first_name_input = self.driver.find_element_by_id('passengerFirstName')
        last_name_input = self.driver.find_element_by_id('passengerLastName')

        conf_input.send_keys(self.confirmation_num)
        first_name_input.send_keys(self.first_name)
        last_name_input.send_keys(self.last_name)

        check_in_btn = self.driver.find_element_by_id('form-mixin--submit-button')
        check_in_btn.click()

        time.sleep(random.randint(2, 5) / 3)

        confirm_btn = self.driver.find_element_by_class_name('air-check-in-review-results--check-in-button')
        confirm_btn.click()

    def send_pass(self):
        text_btn = self.driver.find_element_by_class_name('boarding-pass-options--button-text')
        text_btn.click()

        number_input = self.driver.find_element_by_id('textBoardingPass')
        number_confirmation = self.driver.find_element_by_id('textBoardingPassConfirmation')

        number_input.send_keys(self.number)
        number_confirmation.send_keys(self.number)

        confirm_btn = self.driver.find_element_by_id('form-mixin--submit-button')
        confirm_btn.click()


if __name__ == '__main__':
    checker = SouthwestCheckIn(
        '',  # confirmation number
        '',  # first name
        '',  # last name
        '')  # phone number
    checker.check_in()
    checker.send_pass()
