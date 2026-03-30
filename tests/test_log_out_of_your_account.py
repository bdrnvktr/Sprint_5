import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from constants import USER_LOGIN_DATA

def test_log_out_using_the_log_out_button_in_your_merchant_profile(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
    driver.find_element(*LOGOUT_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGIN_BUTTON)).is_displayed()
