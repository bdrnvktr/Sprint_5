from selenium.webdriver.common.by import By


# КНОПКИ ВХОДА И ЛИЧНЫЙ КАБИНЕТ
LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_CABINET_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка «Личный кабинет»

# ФОРМА РЕГИСТРАЦИИ
REGISTRATION_NAME_FIELD = (By.NAME, 'name')  # Поле «Имя» в форме регистрации
REGISTRATION_EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input[@name = 'name']")  # Поле Email в форме регистрации
REGISTRATION_PASSWORD_FIELD = (By.NAME, 'Пароль')  # Поле пароля в форме регистрации
REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка регистрации
INVALID_PASSWORD_MESSAGE = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Сообщение об ошибке для пароля
LOGIN_IN_REGISTRATION_FORM = (By.XPATH, ".//a[text()='Войти']")  # Кнопка входа в форме регистрации
GO_TO_REGISTRATION = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться» для перехода к форме регистрации

# ФОРМА ВХОДА
LOGIN_EMAIL_FIELD = (By.NAME, 'name')  # Поле email в форме входа
LOGIN_PASSWORD_FIELD = (By.NAME, 'Пароль')  # Поле пароля в форме входа
LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка входа в форме
PASSWORD_RECOVERY_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Кнопка восстановления пароля

# ЛИЧНЫЙ КАБИНЕТ И ВЫХОД
LOGOUT_BUTTON = (By.XPATH, ".//button[@type = 'button' and text()='Выход']")  # Кнопка выхода из аккаунта

# КОНСТРУКТОР И СЕКЦИИ
CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка «Конструктор»
LOGO = (By.XPATH, ".//a[@href = '/']")  # Логотип Stellar Burgers
BUNS_SECTION_BUTTON = (By.XPATH, ".//span[text()='Булки']")  # Кнопка Булки
BUNS_SECTION_TEXT = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")  # проверка после клика Булки внутри конструктора для проверки
SAUCES_SECTION_BUTTON = (By.XPATH, ".//span[text()='Соусы']")  # Кнопка Соусы
SAUCES_SECTION_TEXT = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")  # проверка после клика Соусы внутри конструктора для проверки
TOPPINGS_SECTION_BUTTON = (By.XPATH, ".//span[text()='Начинки']")  # Кнопка Начинки
TOPPINGS_SECTION_TEXT = (By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")  # проверка после клика Начинки внутри конструктора для проверки

# ОБЩИЕ ЭЛЕМЕНТЫ
ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # КНОПКА ОФОРМИТЬ ЗАКАЗ

