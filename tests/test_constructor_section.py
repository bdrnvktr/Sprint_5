import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from constants import USER_LOGIN_DATA
from helpers import generate_user_data


def test_go_to_the_rolls_section(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    driver.find_element(*SAUCES_SECTION_BUTTON).click()
    driver.find_element(*BUNS_SECTION_BUTTON).click()
    assert driver.find_element(*BUNS_SECTION_TEXT).is_displayed()

def test_go_to_the_sauces_section(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    driver.find_element(*SAUCES_SECTION_BUTTON).click()
    assert driver.find_element(*SAUCES_SECTION_TEXT).is_displayed()

def test_go_to_the_toppings_section(driver):
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_FIELD).send_keys(USER_LOGIN_DATA['email'])
    driver.find_element(*LOGIN_PASSWORD_FIELD).send_keys(USER_LOGIN_DATA['password'])
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ORDER_BUTTON))
    driver.find_element(*TOPPINGS_SECTION_BUTTON).click()
    assert driver.find_element(*TOPPINGS_SECTION_TEXT).is_displayed()


