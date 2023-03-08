import pytest
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time


class Test_customer_service():
    def setup_method(self):
        self.driver = webdriver.Firefox()

    def test_customer_service(self):
        self.driver.get('https://prestashop-ta26.multibit.ro/en/')
        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, 'input#email.form-control').send_keys('lucaciubogdansorin@gmail.com')
        self.driver.find_element(By.CSS_SELECTOR, 'textarea#contactform-message.form-control').send_keys(
            'Salut! Vreau sa returnez un produs.')
        self.driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
        time.sleep(3)
        self.driver.get(
            'https://prestashop-ta26.multibit.ro/admin619cii23r/index.php?controller=AdminLogin&token=b65a48f22412c454be6d5d41575880a5&redirect=AdminDashboard#/update-needed?metricsIsUpToDate=true&eventBusIsInstalled=false&eventBusIsUpToDate=false&eventBusIsEnabled=false&accountsIsInstalled=false&accountsIsUpToDate=false&accountsIsEnabled=false')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input#email.form-control").send_keys('ta26@multibit.ro')
        self.driver.find_element(By.CSS_SELECTOR, "input#passwd.form-control").send_keys('TestatareAutomata26')
        self.driver.find_element(By.CSS_SELECTOR,
                                 "button#submit_login.btn.btn-primary.btn-lg.btn-block.ladda-button").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '#subtab-AdminParentCustomerThreads span').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '#subtab-AdminCustomerThreads').click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, '.odd > .column-email').click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        '.message-item-text').text == 'Salut! Vreau sa returnez un produs.'

    def teardown_method(self):
        self.driver.quit()
