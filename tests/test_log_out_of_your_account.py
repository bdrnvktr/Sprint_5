from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_log_out_using_the_log_out_button_in_your_merchant_profile(driver, user_login):
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.NAME, 'name').send_keys(user_login['email'])
    driver.find_element(By.NAME, 'Пароль').send_keys(user_login['password'])
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[@type = 'button' and text()='Выход']")))
    driver.find_element(By.XPATH, ".//button[@type = 'button' and text()='Выход']").click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти']")))
    assert driver.find_element(By.XPATH, ".//button[text()='Войти']").is_displayed()
    driver.quit()    
