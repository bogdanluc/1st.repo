import pytest
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class Test_tap_custom_quantity():
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_tap_custom_quantity(self):
        # accesam pagina
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # selsectam produsul
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(5)").click()
        # crestem cantitatea
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        proceed_button = WebDriverWait(self.driver, 3).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href*='cart?action=show']"))
        proceed_button.click()
        quantity = self.driver.find_element(By.CSS_SELECTOR, ".js-subtotal")
        assert quantity.text == '5 items'

    def teardown_method(self):
        self.driver.quit()
