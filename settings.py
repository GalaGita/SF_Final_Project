import os
from dotenv import load_dotenv
import random


load_dotenv()

# Валидные данные
valid_reg_name = 'Инна'
valid_reg_lastname = 'Ива'
valid_reg_phone = '79876543210'
valid_reg_email = 'inna-iva@mail.ru'
valid_reg_password = '5d%Gh84lj'
invalid_reg_password = '6d%Gh81lj'
valid_name = 'Галина'
valid_lastname = 'Кутыгина'
valid_phone = os.getenv('valid_phone')
valid_email = os.getenv('valid_email')
valid_login = os.getenv('valid_login')
valid_ls = os.getenv('valid_ls')
valid_password = os.getenv('valid_password')


invalid_phone = '799919999991'
invalid_password = '6d%Fs1ty'
invalid_email = 'inga-iva@mail.ru'
invalid_login = 'inga'
invalid_ls = '123456789000'


def russian_chars(num):
    text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def english_chars(num):
    text = 'abcdefghijklmnopqrstuvwxyz'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def number_chars(num):
    text = '0123456789'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string

def special_chars(num):
    text = '|/!@#$%^&*()-_=+`~?"№;:[]{}'
    rand_string = ''.join(random.choice(text) for i in range(num))
    return rand_string


def password_random(num):
    text = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    text1 = 'abcdefghijklmnopqrstuvwxyz'
    text2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text3 = '+-/*!&$#?=@<>1234567890'
    rand_string = ''.join(random.choice(text1) for i in range(1)) + ''.join(random.choice(text2) for i in range(1)) \
                  + ''.join(random.choice(text3) for i in range(1)) + ''.join(random.choice(text) for i in range(num-3))
    return rand_string
