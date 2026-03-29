from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_switching_to_the_constructor(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@type = 'button' and text()='Выход']")))
    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").is_displayed()
    driver.quit()    

def test_switching_to_the_stellar_burgers_logo(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@type = 'button' and text()='Выход']")))
    driver.find_element(By.XPATH, ".//a[@href = '/']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").is_displayed()
    driver.quit()    