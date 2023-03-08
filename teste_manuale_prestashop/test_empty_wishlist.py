import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


class Test_empty_wishlist():
    def setup_method(self):
        self.driver = webdriver.Firefox()

    def test_empty_wishlist(self):
        self.driver.get('https://prestashop-ta26.multibit.ro/en/')
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        # click casuta email
        self.driver.find_element(By.ID, "field-email").click()
        # introduc parola
        self.driver.find_element(By.ID, "field-password").send_keys("paroladetest")
        # introduc email
        self.driver.find_element(By.ID, "field-email").send_keys("lucaciubogdansorin@gmail.com")
        # click login
        self.driver.find_element(By.ID, "submit-login").click()
        # click categorie produse
        self.driver.find_element(By.CSS_SELECTOR, "#category-9 > .dropdown-item").click()
        self.driver.find_element(By.CSS_SELECTOR, ".h3").click()
        product = self.driver.find_element(By.CSS_SELECTOR, ".h3").get_attribute("innerText")
        # adaug produs in wishlist
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-button-add .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item").click()
        # accesez lista
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        self.driver.find_element(By.CSS_SELECTOR, "#wishlist-link .material-icons").click()
        mywishlist = WebDriverWait(self.driver, 5).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".wishlist-list-item-title"))
        mywishlist.click()
        # verific ca produsul e in lista de dorinte
        assert product.upper() in self.driver.page_source.upper()
        time.sleep(1)
        # sterg produsul din lista
        self.driver.find_element(By.CSS_SELECTOR, "button.wishlist-button-add").click()
        time.sleep(1)
        remove_button = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(By.XPATH,
                                                                                      "/html/body/main/footer/div[2]/div/div[1]/div[5]/div[1]/div/div/div[3]/button[2]"))
        remove_button.click()
        time.sleep(2)
        assert self.driver.find_element(By.CSS_SELECTOR, ".wishlist-list-empty").text == "No products found"

    def teardown_method(self):
        self.driver.quit()
