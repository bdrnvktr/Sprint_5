from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_go_to_the_rolls_section(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
    assert driver.find_element(By.XPATH, ".//h2[text()='Булки']").is_displayed()
    driver.quit()    

def test_go_to_the_sauces_section(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    assert driver.find_element(By.XPATH, ".//h2[text()='Соусы']").is_displayed()
    driver.quit()    

def test_go_to_the_toppings_section(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    assert driver.find_element(By.XPATH, ".//h2[text()='Начинки']").is_displayed()
    driver.quit()