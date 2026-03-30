import random
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

def generate_email(name='budarin', surname='viktor', cohort='42'):
    digits = ''.join(random.choices(string.digits, k=3))
    return f'{name}_{surname}_{cohort}_{digits}@yandex.ru'

def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(8))

def generate_user_data():
    return {
        'name': 'Viktor',
        'email': generate_email(),
        'password': generate_password()
    }