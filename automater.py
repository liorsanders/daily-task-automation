import constants
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
import time

class Connector:
    def connect_driver(self):
        self.driver = webdriver.Chrome(executable_path=constants.DRIVER_PATH)

    def get_bank_info(self, username: str, password: str) -> float:
        self.driver.get(constants.BANK_LINK)
        self.driver.find_element_by_css_selector(constants.BANK_USERNAME_SELECTOR).send_keys(username)      
        self.driver.find_element_by_css_selector(constants.BANK_PASSWORD_SELECTOR).send_keys(password)
        self.driver.find_element_by_css_selector(constants.BANK_LOGIN_BTN_SELECTOR).click()
        val = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, constants.BANK_BALANCE_SELECTOR)))
        return float(re.sub(',', '', val.text))

