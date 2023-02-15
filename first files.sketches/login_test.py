# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# username
chrome.find_element(By.ID, 'username').send_keys('tomsmith')

sleep(3)

# pass
chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')

sleep(3)

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()

sleep(3)

chrome.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()

sleep(3)

chrome.quit(3)

