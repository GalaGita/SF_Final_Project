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


def test_auth_user_phone(browser):
    """Авторизация по номеру телефона с валидными данными"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'

def test_auth_user_mail(browser):
    """Авторизация по электронной почте  с валидными данными"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(valid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'

def test_auth_user_login(browser):
    """Авторизация по логину с валидными данными"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(valid_login)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'

def test_auth_user_ls(browser):
    """Авторизация по лицевому счету с валидными данными"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(valid_ls)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.TAG_NAME, 'h3').text == 'Учетные данные'

def test_auth_invalid_phone(browser):
    """Авторизация по невалидному номеру телефона"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(invalid_phone)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_invalid_password(browser):
    """Авторизация по номеру телефона с невалидным паролем"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-phone').click()
    driver.find_element(By.ID, 'username').send_keys(valid_phone)
    driver.find_element(By.ID, 'password').send_keys(invalid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_invalid_mail(browser):
    """Авторизация по невалидной электронной почте"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-mail').click()
    driver.find_element(By.ID, 'username').send_keys(invalid_email)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_invalid_login(browser):
    """Авторизация по невалидному логину"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(invalid_login)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'

def test_auth_invalid_ls(browser):
    """Авторизация по невалидному лицевому счету"""
    driver = browser
    driver.get('https://b2c.passport.rt.ru')
    element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, 'kc-login')))
    driver.find_element(By.ID, 't-btn-tab-login').click()
    driver.find_element(By.ID, 'username').send_keys(invalid_ls)
    driver.find_element(By.ID, 'password').send_keys(valid_password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    browser.implicitly_wait(5)
    assert driver.find_element(By.ID, 'form-error-message').text == 'Неверный логин или пароль'
