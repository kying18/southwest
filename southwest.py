from selenium import webdriver


def main():
    driver = webdriver.Chrome()
    driver.get('https://www.southwest.com/air/check-in/index.html')

    conf_num = driver.find_element_by_id('confirmationNumber')
    first_name = driver.find_element_by_id('passengerFirstName')
    last_name = driver.find_element_by_id('passengerLastName')

    conf_num.send_keys('TestNum')
    first_name.send_keys('Y')
    last_name.send_keys('Cubed')

    submit = driver.find_element_by_id('form-mixin--submit-button')
    submit.click()

    confirm = driver.find_element_by_class_name('air-check-in-review-results--check-in-button')
    confirm.click()

    text_btn = driver.find_element_by_class_name('boarding-pass-options--button-text')
    text_btn.click()

    phone = driver.find_element_by_id('textBoardingPass')
    phone_conf = driver.find_element_by_id('textBoardingPassConfirmation')

    phone.send_keys('1234567890')
    phone_conf.send_keys('1234567890')

    confirm_btn = driver.find_element_by_id('form-mixin--submit-button')
    confirm_btn.click()


if __name__ == '__main__':
    main()
