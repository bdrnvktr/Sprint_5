from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_registration(driver, user_data):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_data['name'])
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@name = 'name']").send_keys(user_data['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_data['password'])
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
    button_login = driver.find_elements(By.XPATH, "//button[text()='Войти']")
    assert len(button_login) == 1
    assert driver.find_element(By.XPATH, "//button[text()='Войти']").is_displayed()
    driver.quit()

def test_invalid_password_registration(driver, user_data):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_data['name'])
    driver.find_element(By.XPATH, ".//fieldset[2]//input[@name = 'name']").send_keys(user_data['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys('123')
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    assert driver.find_element(By.XPATH, ".//p[text()='Некорректный пароль']").is_displayed()
    driver.quit()