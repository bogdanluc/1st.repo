import pytest
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains



class Test_enter_custom_quantity():
    def setup_method(self):
        self.driver = webdriver.Firefox()

    def test_enter_custom_quantity(self):
        # accesam pagina
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # selsectam produsul
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(7)").click()
        quantity_field = self.driver.find_element(By.ID, "quantity_wanted")
        #initializam obiectul ActionChains pentru  a folosi dublu-click
        actions = ActionChains(self.driver)
        #dublu click pe casuta cantitatii
        actions.double_click(quantity_field).perform()
        time.sleep(1)
        #introducem cantitatea - 7
        quantity_field.send_keys(7)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        proceed_button = WebDriverWait(self.driver, 3).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href*='cart?action=show']"))
        proceed_button.click()
        quantity = self.driver.find_element(By.CSS_SELECTOR, ".js-subtotal")
        assert quantity.text == '7 items'

    def teardown_method(self):
        self.driver.quit()