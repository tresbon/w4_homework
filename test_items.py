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


def choose_clickable_good(browser, goods_links):

    '''Recusrively chooses clickable good'''

    good = choice(goods_links)

    browser.get(good)

    if not browser.find_elements(By.CSS_SELECTOR, \
    'button.btn-add-to-basket'):

        choose_clickable_good(browser, goods_links)

    return good

def test_order_button_with_lang(browser,lang):

    goods_links = get_goods_from_sitemap(lang)

    good = choose_clickable_good(browser, goods_links)

    browser.get(good)

    assert browser.find_elements(By.CSS_SELECTOR, \
    'button.btn-add-to-basket'), f'For lang {lang} clickable good wasn`t found'