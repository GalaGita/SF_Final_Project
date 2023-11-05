import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import NoSuchElementException
from settings import *

@pytest.fixture(autouse=True)
def browser():
   driver = webdriver.Chrome('E://Python/SF_FinalProject/chromedriver.exe')

   driver.get('https://b2c.passport.rt.ru')

   yield driver

   driver.quit()


def test_reg_page(browser):
   """Проверка, что страница "Регистрация" загружается """
   driver = browser
   driver.get('https://b2c.passport.rt.ru')
   element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'kc-register')))
   driver.find_element(By.ID, 'kc-register').click()
   driver.implicitly_wait(5)
   assert driver.find_element(By.TAG_NAME, 'h1').text == 'Регистрация'
   assert driver.find_element(By.TAG_NAME, 'p').text == 'Личные данные'
   assert driver.find_element(By.XPATH, '//button[@type="submit"]')

def test_reg_valid_phone(browser):
    """Проверяем, что при регистрации по телефону с валидными данными система перенаправляет пользователя 
        на страницу ввода кода"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, 'firstName').send_keys(valid_reg_name)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_reg_lastname)
    driver.find_element(By.ID, 'address').send_keys(valid_reg_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_reg_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_reg_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(3)
    assert driver.find_element(By.CLASS_NAME, "register-confirm-form")

def test_reg_valid_email(browser):
    """Проверяем, что при регистрации по email с валидными данными система перенаправляет пользователя
    на страницу ввода кода"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, 'firstName').send_keys(valid_reg_name)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_reg_lastname)
    driver.find_element(By.ID, 'address').send_keys(valid_reg_email)
    driver.find_element(By.ID, 'password').send_keys(valid_reg_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_reg_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(3)
    assert driver.find_element(By.CLASS_NAME, "register-confirm-form")

def test_reg_empty_fields(browser):
    """Проверяем, что с пустыми полями регистрация не проходит (под полями выдается 5 сообщений об ошибках)"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    error = driver.find_elements(By.CSS_SELECTOR, '.rt-input-container--error')
    time.sleep(3)
    assert len(error) == 5

@pytest.mark.parametrize("negative_name_input", [number_chars(5), special_chars(7), english_chars(6),
                                                 russian_chars(1), russian_chars(31)],
                         ids=['5 цифр', '7 спецсимволов', '6 символов латиницы',
                              '1 символ кириллицы', '31 символ кириллицы'])
def test_reg_incorrect_name(negative_name_input, browser):
    """Проверяем, что система выдает подсказку при вводе в поле "Имя" символов, не соответствующих требованиям"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.NAME, "firstName").send_keys(negative_name_input)
    driver.find_element(By.NAME, "lastName").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == "Необходимо заполнить поле " \
                                                                                  "кириллицей. От 2 до 30 символов."

@pytest.mark.parametrize("incorrect_lastname_input", [number_chars(5), special_chars(7), english_chars(6),
                                            russian_chars(1), russian_chars(31)],
                         ids=['5 цифр', '7 спецсимволов', '6 символов латиницы',
                              '1 символ кириллицы', '31 символ кириллицы'])
def test_reg_incorrect_lastname(incorrect_lastname_input, browser):
    """Проверяем, что система выдает подсказку при вводе в поле "Фамилия" символов, не соответствующих требованиям"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "lastName").send_keys(incorrect_lastname_input)
    driver.find_element(By.NAME, "firstName").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta").text == "Необходимо заполнить поле " \
                                                                                  "кириллицей. От 2 до 30 символов."

@pytest.mark.parametrize("incorrect_email_input", ['@mail.ru', 'inga@', 'inga.mail.ru', 'inga@mail'],
                         ids=['без локальной части', 'без доменной части', 'без @', 'без домена верхнего уровня'])
def test_reg_incorrect_email(incorrect_email_input, browser):
    """Проверяем, что система выдает подсказку при вводе в поле "E-mail или мобильный телефон"
    email, не соответствующий требованиям"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.ID, "address").send_keys(incorrect_email_input)
    driver.find_element(By.ID, "password").click()
    assert driver.find_element(By.CLASS_NAME,
                               "rt-input-container__meta").text == "Введите телефон в формате +7ХХХХХХХХХХ " \
                                                                   "или +375XXXXXXXXX,или email в формате " \
                                                                   "example@email.ru"

@pytest.mark.parametrize("incorrect_phone_input", ['7894561230', '3751234567890', '89874561230'],
                         ids=['10 цифр', '13 цифр', '11 цифр начиная с 8'])
def test_reg_incorrect_phone(incorrect_phone_input, browser):
    """"Проверяем, что система выдает подсказку при вводе в поле "E-mail или мобильный телефон"
    телефона, не соответствующего требованиям"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.ID, "address").send_keys(incorrect_phone_input)
    driver.find_element(By.ID, "password").click()
    assert driver.find_element(By.CLASS_NAME,
                               "rt-input-container__meta").text == "Введите телефон в формате +7ХХХХХХХХХХ " \
                                                                   "или +375XXXXXXXXX, или email в формате " \
                                                                   "example@email.ru"

@pytest.mark.parametrize("incorrect_password_input", [russian_chars(8), english_chars(8), special_chars(8),
                                                      number_chars(8), 'R4985123', 'SQWhjkug', password_random(7),
                                                      password_random(64), password_random(21)],
                         ids=['8 букв кириллицы', '8 букв латиницы', '8 спецсимволов', '8 цифр',
                              '7 цифр и 1 заглавная буква латиницы', '3 заглавных и 5 строчных букв латиницы',
                              '7 символов, включая спецсимволы, цифры, заглавные и строчные буквы латиницы',
                              '64 символа, включая спецсимволы, цифры, заглавные и строчные буквы латиницы',
                              '21 символ, включая спецсимволы, цифры, заглавные и строчные буквы латиницы'])
def test_reg_incorrect_password(incorrect_password_input, browser):
    """Проверяем, что система выдает подсказку при вводе в поле "Пароль" пароля, не соответствующего требованиям"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.ID, "password").send_keys(incorrect_password_input)
    driver.find_element(By.ID, "address").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta")

def test_reg_incorrect_password_confirm(browser):
    """Проверяем, что система выдает подсказку при вводе в поле 'Подтверждение пароля'
    значения, отличного от пароля в поле 'Пароль'"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, "kc-register").click()
    driver.find_element(By.NAME, "firstName").clear()
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.ID, "password").send_keys(valid_reg_password)
    driver.find_element(By.ID, "password-confirm").send_keys(invalid_reg_password)
    driver.find_element(By.ID, "address").click()
    assert driver.find_element(By.CLASS_NAME, "rt-input-container__meta")

def test_reg_non_unique_email(browser):
    """Проверяем, что при регистрации с неуникальным email появляется оповещающая форма"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, 'firstName').send_keys(valid_reg_name)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_reg_lastname)
    driver.find_element(By.ID, 'address').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_reg_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_reg_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h2').text == 'Учётная запись уже существует'

def test_reg_non_unique_phone(browser):
    """Проверяем, что при регистрации с неуникальным телефоном появляется оповещающая форма"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.ID, 'kc-register')))
    driver.find_element(By.ID, 'kc-register').click()
    driver.find_element(By.NAME, 'firstName').send_keys(valid_reg_name)
    driver.find_element(By.NAME, 'lastName').send_keys(valid_reg_lastname)
    driver.find_element(By.ID, 'address').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_reg_password)
    driver.find_element(By.ID, 'password-confirm').send_keys(valid_reg_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h2').text == 'Учётная запись уже существует'
