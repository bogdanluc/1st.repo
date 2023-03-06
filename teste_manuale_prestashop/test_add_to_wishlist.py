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


class Test_Add_to_wishlist():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.product_detail_url = None

    def teardown_method(self, method):
        if self.product_detail_url is not None:
            self.driver.get(self.product_detail_url)
            self.driver.find_element(By.CSS_SELECTOR, ".wishlist-button-add > .material-icons").click()
        self.driver.quit()


    def test_add_to_wishlist(self):
        #accesam pagina web
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # setam rezolutia paginii
        self.driver.set_window_size(1168, 637)
        # accesam pagina de logare
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        # click pe casuta email
        self.driver.find_element(By.ID, "field-email").click()
        # introducem parola
        self.driver.find_element(By.ID, "field-password").send_keys("paroladetest")
        # introducem email
        self.driver.find_element(By.ID, "field-email").send_keys("lucaciubogdansorin@gmail.com")
        # click pe login
        self.driver.find_element(By.ID, "submit-login").click()
        # click pe categoria de produse
        self.driver.find_element(By.CSS_SELECTOR, "#category-3 > .dropdown-item").click()
        # selectare produs
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2) img").click()
        #cream variabila produsului
        product_name = self.driver.find_element(By.TAG_NAME, "h1").get_attribute("innerText")
        # click pe butonul wishlist
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-button-add > .material-icons").click()
        self.product_detail_url = self.driver.current_url
        # adaugam produsul in lista de dorinte
        wishlist_item = WebDriverWait(self.driver, 30).until(
            lambda d: d.find_element(By.CSS_SELECTOR, ".wishlist-list-item > p"))
        wishlist_item.click()
        # accesam contul
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        # accesam wishlist
        self.driver.find_element(By.CSS_SELECTOR, "#wishlist-link .material-icons").click()
        product = WebDriverWait(self.driver, 15).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item-title"))
        product.click()
        # 15 | click | css=.wishlist-products-list |
        # product = WebDriverWait(self.driver, 15).until(
        #     lambda driver: driver.find_element(By.CSS_SELECTOR, ".wishlist-products-list"))
        # product.click()
        self.driver.implicitly_wait(5)
        wishlist_products = self.driver.find_element(By.CLASS_NAME, "wishlist-products-list")
        wishlist_titles = wishlist_products.find_elements(By.CLASS_NAME, "wishlist-product-title")
        titles = [t.get_attribute("innerText").lower() for t in wishlist_titles]
        assert product_name.lower() in titles
