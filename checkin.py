from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random


class SouthwestCheckIn:
    def __init__(self, confirmation_num, first_name, last_name):
        self.confirmation_num = confirmation_num
        self.first_name = first_name
        self.last_name = last_name
        options = Options()
        options.add_experimental_option("prefs", {
          "download.default_directory": r"C:\Users\xxx\downloads\Test",
          "download.prompt_for_download": False,
          "download.directory_upgrade": True,
          "safebrowsing.enabled": True
        })
        self.driver = webdriver.Chrome(chrome_options=options)
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

        confirm_btn = self.driver.find_element_by_id('form-mixin--submit-button')
        confirm_btn.click()


if __name__ == '__main__':
    checker = SouthwestCheckIn('123456', 'Yueyang', 'Ying')
    checker.check_in()
