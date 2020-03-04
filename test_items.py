from random import choice
from lxml import etree
from requests import request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_goods_from_sitemap(lang):

    '''Get list of goods urls'''

    root = etree.fromstring(request('GET',\
        'http://selenium1py.pythonanywhere.com/sitemap.xml'\
            ).content)

    products_sitemap = [i[0].text.replace('example.com',\
        'selenium1py.pythonanywhere.com') for i in root
        if f'products-{lang}.' in i[0].text][0]

    root = etree.fromstring(request('GET',\
        products_sitemap).content)

    goods_links = [i[0].text.replace('example.com',\
        'selenium1py.pythonanywhere.com') for i in root]

    return goods_links


def choose_clickable_good(browser, goods_links,\
    recurtion = False):

    '''Chooses random good'''

    good = choice(goods_links)

    if recurtion:
        browser.get(good)

        #If no button in good - start recursion
        if not browser.find_elements(By.CSS_SELECTOR, \
        'button.btn-add-to-basket'):

            choose_clickable_good(browser, goods_links, True)

    return good

def test_random_product_has_order_button(browser,lang):
    '''
    Тест - у товара есть кнопка добавления
    1. Перейти в случайный товар с учётом языка
    2. Выбрать случайный товар
    3. Проверить что у товара есть кнопка'''
    
    #Выбираем случайный товар
    goods_links = get_goods_from_sitemap(lang)
    good = choose_clickable_good(browser, goods_links)

    #Переходим на страницу товара
    browser.get(good)

    assert browser.find_elements(By.CSS_SELECTOR, \
    'div.basket-mini a.btn'), f'''Product {good} hasnt
    clickable button'''


#Тест короткий и скучный, поэтому я написал ещё
def test_random_product_is_orderable(browser,lang):
    '''
    Тест что товар добавляется в корзину
    1. Перейти в случайный товар с учётом языка
    2. Выбрать случайный товар с активной
    кнопкой добавления в корзину
    3. Добавить в корзину
    4. Перейти в корзину
    5. Проверить что товар появился в корзине (
        ссыка на товар есть среди ссылок на
        товары в корзине
    )
    '''
    
    #Выбираем случайный товар
    goods_links = get_goods_from_sitemap(lang)
    good = choose_clickable_good(browser, goods_links,True)

    #Переходим на страницу товара
    browser.get(good)

    #Добавляем товар в корзину
    browser.find_element(By.CSS_SELECTOR, \
    'button.btn-add-to-basket').click()

    #Переходим в корзину
    browser.find_element(By.CSS_SELECTOR, \
        'div.basket-mini a.btn').click()

    #Собираем ссылки на товары добавленные в корзину
    basket_links = browser.find_elements(By.CSS_SELECTOR, \
        '.basket-items a')
    basket_links = [i.get_attribute('href') for i in \
        basket_links]
    
    assert good in basket_links, f'''Product {good} addable
    to basket'''