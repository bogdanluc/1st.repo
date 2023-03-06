import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains


# definim clasa
class Test_color_selection():
    # definim metoda de initializare
    def setup_method(self):
        self.driver = webdriver.Firefox()

    # definim metoda de test
    def test_color_selection(self):
        # accesam pagina
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # deschidem pagina cu toate produsele
        self.driver.find_element(By.CSS_SELECTOR, ".all-product-link").click()
        # cream variabila produsului
        bear_cushion = self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(10)")
        # cream obiectul actions cu ajutorul caruia vom naviga cu cursorul pe pagina
        actions = ActionChains(self.driver)
        # time.sleep(2)
        # cream variabila casutei de selectare a culorii
        color = self.driver.find_element(By.CSS_SELECTOR, ".color[title='White']")
        # WebDriverWait(self.driver,2)
        # cream variabila locatiei produsului
        location = bear_cushion.location['y']
        # time.sleep(2)
        # facem scroll pe pagina
        self.driver.execute_script(f"window.scrollTo(0, {location})")
        # time.sleep(2)
        # navigam pe meniul de quick view al produsului dorit
        actions.move_to_element(bear_cushion).perform()
        # time.sleep(2)
        # selectam culoarea produsului din meniul Quickview
        actions.move_to_element(color).click()
        # time.sleep(2)
        color.click()
        # time.sleep(2)
        # adaugam produsul in cos
        add_button = WebDriverWait(self.driver, 5).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary.add-to-cart"))
        add_button.click()
        # cream variabila proceed pentru a inainta catre checkout
        proceed = WebDriverWait(self.driver, 3).until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn.btn-primary"))
        proceed.click()
        # verificam ca produsul selectat are culoarea aleasa - alb
        assert self.driver.find_element(By.CSS_SELECTOR, ".color > .value").text == "White"
        # incheiam cu metoda de curatare

    def teardown_method(self):
        self.driver.quit()
