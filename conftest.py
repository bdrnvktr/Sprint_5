import pytest
from selenium import webdriver
from utils import generate_email, generate_password

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    return driver

@pytest.fixture
def user_data():
    return {
        'email': generate_email(),
        'password': generate_password(),
        'name': 'Viktor'
    }

@pytest.fixture
def user_login():
    return {
        'email': 'budarin42@mail.ru',
        'password': '123456'

    }