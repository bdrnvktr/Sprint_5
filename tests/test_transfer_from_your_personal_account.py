
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from constants import USER_LOGIN_DATA

def test_switching_to_the_constructor(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
    driver.find_element(*CONSTRUCTOR_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

def test_switching_to_the_stellar_burgers_logo(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(LOGOUT_BUTTON))
    driver.find_element(*LOGO).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON)).is_displayed()