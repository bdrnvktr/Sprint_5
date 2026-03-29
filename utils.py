import random
import string

def generate_email(name='budarin', surname='viktor', cohort='42'):
    digits = ''.join(random.choices(string.digits, k=3))
    return f'{name}_{surname}_{cohort}_{digits}@yandex.ru'

def generate_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(8))