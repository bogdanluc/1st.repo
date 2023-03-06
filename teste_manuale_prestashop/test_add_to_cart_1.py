import time
import unittest
import pytest
import selenium
import self as self
import until as until
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import json


class Test_add_to_cart1():
    #@pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Firefox()

    # def tearDown(self):
    #     self.driver.quit()

    def test_add_to_cart1(self):
        # accesam pagina web prestashop
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # cautam produsul dorit
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2)").click()
        # adaugam variabila produsului selectat
        product = self.driver.find_element(By.CSS_SELECTOR, ".h1").get_attribute("innerText")
        # click pe buton de adaugare in cos
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # click pe buton de continuare la cos
        # self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click() -> NoSuchElementException
        proceed = WebDriverWait(self.driver, 3).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary"))
        proceed.click()
        #verificam daca produsul se afla in cosul de cumparaturi
        assert product.lower() in self.driver.page_source.lower()
        time.sleep(3)
        self.driver.close()

    def teardown_method(self):
        self.driver.quit()
