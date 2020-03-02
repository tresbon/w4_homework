#Импортируем библиотеки
from selenium import webdriver
from random import choice
import time
from lxml import etree
import re
from requests import request
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_mail():
    '''Generates email with 5 letters @ 3 letters . 3 letters'''
    letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
    return ''.join(choice(letters) for l in range(5)) + '@' +\
        ''.join([choice(letters) for l in range(3)])  + '.' +\
        ''.join([choice(letters) for l in range(3)]) 

def generate_pass(nletters:int,ndigits:int):
    '''Generates password with nletters and ndigids'''
    letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
    digits = [str(i) for i in range (10)]
    return ''.join([choice(letters) for l in range(nletters)]) + \
    ''.join([choice(digits) for d in range(ndigits)])

mail = generate_mail()
password = generate_pass(5,4)

'''
Тест №1 Регистрация на сайте
1. Перейти по адресу http://selenium1py.pythonanywhere.com/ru/
2. Найти элемент a#login_link и перейти по нему
3. Заполнить поле #id_registration-email валидным e-mail
4. Заполнить поле #id_registration-password1 паролем
(9 символов хотя бы одна цифра и хотя бы одна буква)
5. Повторить пароль в поле #id_registration-password2
6. Выбрать кнопку form#register_form button[name='registration_submit']
и кликнуть
7. Удостовериться что появилось сообщение 'Спасибо за регистрацию!'
'''

try:
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/ru/')

    l_link = browser.find_element_by_css_selector('a#login_link')
    l_link.click()

    email = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, \
            "#id_registration-email"))
    )
    email.send_keys(mail)

    pass1 = browser.find_element_by_css_selector(\
        '#id_registration-password1')
    pass1.send_keys(password)

    pass2 = browser.find_element_by_css_selector(\
        '#id_registration-password2')
    pass2.send_keys(password)

    button = browser.find_element_by_css_selector(\
        "form#register_form button[name='registration_submit']")
    button.click()

    success_message = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, \
            "div#messages div.alertinner.wicon"))
    )

    assert 'Спасибо за регистрацию!' in success_message.text
    print('Test #1 Sing Up passed')