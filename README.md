Бударин Виктор
Когорта 42
Sprint_5 — Автотесты для Stellar Burgers

Автоматизированные тесты для веб‑приложения Stellar Burgers с использованием Selenium.

Установка

1. Установите зависимости: pip install selenium pytest
2. Убедитесь, что установлены браузеры: Google Chrome и Mozilla Firefox.
3. Запустите тесты: pytest tests/ -v

Структура проекта

- tests/ — директория с тестами.
- conftest.py — фикстуры для тестов.
- utils.py — вспомогательные функции (генераторы логинов и паролей).

========================================== test session starts ===========================================
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\Admin\AppData\Local\Python\pythoncore-3.14-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Sprint_5
plugins: cov-7.0.0
collected 13 items

tests/test_constructor_section.py::test_go_to_the_rolls_section PASSED                                                               [  7%]
tests/test_constructor_section.py::test_go_to_the_sauces_section PASSED                                                              [ 15%]
tests/test_constructor_section.py::test_go_to_the_toppings_section PASSED                                                            [ 23%]
tests/test_log_out_of_your_account.py::test_log_out_using_the_log_out_button_in_your_merchant_profile PASSED                         [ 30%]
tests/test_login.py::test_the_login_account_button PASSED                                                                            [ 38%]
tests/test_login.py::test_login_with_the_personal_account_button PASSED                                                              [ 46%]
tests/test_login.py::test_login_button_in_the_registration_form PASSED                                                               [ 53%]
tests/test_login.py::test_login_button_in_the_password_recovery_form PASSED                                                          [ 61%]
tests/test_personal_account.py::test_click_through_to_your_personal_account PASSED                                                   [ 69%]
tests/test_registration.py::test_successful_registration PASSED                                                                      [ 76%]
tests/test_registration.py::test_invalid_password_registration PASSED                                                                [ 84%]
tests/test_transfer_from_your_personal_account.py::test_switching_to_the_constructor PASSED                                          [ 92%]
tests/test_transfer_from_your_personal_account.py::test_switching_to_the_stellar_burgers_logo PASSED                                 [100%]

===================================== 13 passed in 76.27s (0:01:16) ====================================