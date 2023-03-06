import pytest
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Test_add_to_cart2():
    # definim metoda de initializare
    def setup_method(self):
        self.driver = webdriver.Chrome()

    # definim metoda de test
    def test_add_to_cart2(self):
        # deschidem pagina web
        self.driver.get("https://prestashop-ta26.multibit.ro/en/")
        # deschidem pagina completa cu produse
        self.driver.find_element(By.CSS_SELECTOR, ".all-product-link").click()
        # selectam produsul dorit
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(9)")
        # cream variabila produsului
        cushion = self.driver.find_element(By.CSS_SELECTOR, ".h1").get_attribute("innerText")
        # adaugam produsul in cos
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # continuam catre cosul de cumparaturi
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        # verificam daca produsul selectat se gaseste in cosul de cumparaturi
        assert cushion.lower() in self.driver.page_source.lower()
        time.sleep(2)
        self.driver.close()
    #definim metoda de curatare
    def teardown_method(self):
        self.driver.quit()
