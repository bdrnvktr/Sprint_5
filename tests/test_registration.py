import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import generate_user_data

def test_successful_registration(driver):
    user_data = generate_user_data()
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*GO_TO_REGISTRATION).click()
    driver.find_element(*REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
    driver.find_element(*REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
    driver.find_element(*REGISTRATION_PASSWORD_FIELD).send_keys(user_data['password'])
    driver.find_element(*REGISTER_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON)).is_displayed()


def test_invalid_password_registration(driver):
    user_data = generate_user_data()
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*GO_TO_REGISTRATION).click()
    driver.find_element(*REGISTRATION_NAME_FIELD).send_keys(user_data['name'])
    driver.find_element(*REGISTRATION_EMAIL_FIELD).send_keys(user_data['email'])
    driver.find_element(*REGISTRATION_PASSWORD_FIELD).send_keys('123')
    driver.find_element(*REGISTER_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(INVALID_PASSWORD_MESSAGE)).is_displayed()