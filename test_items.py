import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def  test_basket_button(browser):
    
    
    browser.get(link)
    #всего лишь надо раскомментить, чтобы сэкономить время
    #time.sleep(30)
   
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
    )
    
    assert button, "Button not found"