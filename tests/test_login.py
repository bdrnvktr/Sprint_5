import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from constants import USER_LOGIN_DATA

def test_the_login_account_button(driver):
    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

def test_login_with_the_personal_account_button(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

def test_login_button_in_the_registration_form(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*GO_TO_REGISTRATION).click()
    driver.find_element(*LOGIN_IN_REGISTRATION_FORM).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON)).is_displayed()

def test_login_button_in_the_password_recovery_form(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*PASSWORD_RECOVERY_LINK).click()
    driver.find_element(*LOGIN_IN_REGISTRATION_FORM).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON)).is_displayed()