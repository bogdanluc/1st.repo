import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import time

class Test_product_price():

    def setup_method(self):
        self.driver = webdriver.Firefox()

    def test_product_price(self):
        #accesam pagina web
        self.driver.get('https://prestashop-ta26.multibit.ro/en/')
        #accesam toate produsele disponibile pe pagina
        self.driver.find_element(By.CSS_SELECTOR, ".all-product-link").click()
        #accesam pagina a doua
        self.driver.find_element(By.CSS_SELECTOR, ".next").click()
        time.sleep(2)
        #selectam produsul
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2)").click()
        product_price = self.driver.find_element(By.CSS_SELECTOR, '.product-price').text
        #verificam pretul produsui
        assert product_price == 'lei10.71'
        #mai adaugam 2 bucati
        spinup_button = self.driver.find_element(By.CSS_SELECTOR, '.touchspin-up')
        spinup_button.click()
        spinup_button.click()
        #adaugam produsul in cos
        self.driver.find_element(By.CSS_SELECTOR, '.add-to-cart').click()
        checkout_button = WebDriverWait(self.driver, 3).until(lambda driver:driver.find_element(By.CSS_SELECTOR, '.cart-content-btn > .btn.btn-primary'))
        checkout_button.click()
        time.sleep(1)
        quantity = self.driver.find_element(By.CSS_SELECTOR, ".js-subtotal")
        total_price = self.driver.find_element(By.CSS_SELECTOR, ".value").text
        assert quantity.text == '3 items'
        assert total_price == 'lei32.13'

    def teardown_method(self):
        self.driver.quit()