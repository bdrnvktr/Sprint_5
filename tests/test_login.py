from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_the_login_account_button(driver, user_login):
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").is_displayed()
    driver.quit()

def test_login_with_the_personal_account_button(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").is_displayed()
    driver.quit()

def test_login_button_in_the_registration_form(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").is_displayed()
    driver.quit()

def test_login_button_in_the_password_recovery_form(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()
    driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").is_displayed()
    driver.quit()