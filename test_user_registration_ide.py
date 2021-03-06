# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegtest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_regtest(self):
    # Test name: reg_test
    # Step # | name | target | value | comment
    # 1 | open | /ru/ |  | 
    self.driver.get("http://selenium1py.pythonanywhere.com/ru/")
    # 2 | setWindowSize | 1402x797 |  | 
    self.driver.set_window_size(1402, 797)
    # 3 | click | id=login_link |  | 
    self.driver.find_element(By.ID, "login_link").click()
    # 4 | click | id=id_login-username |  | 
    self.driver.find_element(By.ID, "id_login-username").click()
    # 5 | type | id=id_login-username | sdaf@dsafafhj.cdf | 
    self.driver.find_element(By.ID, "id_login-username").send_keys("sdaf@dsafafhj.cdf")
    # 6 | click | id=id_login-password |  | 
    self.driver.find_element(By.ID, "id_login-password").click()
    # 7 | type | id=id_login-password | 12345qazwsx | 
    self.driver.find_element(By.ID, "id_login-password").send_keys("12345qazwsx")
    # 8 | click | name=login_submit |  | 
    self.driver.find_element(By.NAME, "login_submit").click()
    # 9 | click | id=id_registration-email |  | 
    self.driver.find_element(By.ID, "id_registration-email").click()
    # 10 | type | id=id_registration-email | asdf@sadf.adsf | 
    self.driver.find_element(By.ID, "id_registration-email").send_keys("asdf@sadf.adsf")
    # 11 | click | id=id_registration-password1 |  | 
    self.driver.find_element(By.ID, "id_registration-password1").click()
    # 12 | type | id=id_registration-password1 | shQYqyVER2zfMRc | 
    self.driver.find_element(By.ID, "id_registration-password1").send_keys("shQYqyVER2zfMRc")
    # 13 | type | id=id_registration-password2 | shQYqyVER2zfMRc | 
    self.driver.find_element(By.ID, "id_registration-password2").send_keys("shQYqyVER2zfMRc")
    # 14 | click | name=registration_submit |  | 
    self.driver.find_element(By.NAME, "registration_submit").click()
    # 15 | click | css=html |  | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
  
