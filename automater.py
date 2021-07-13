import constants
from selenium import webdriver
import time
import bs4
import requests


class Connector:
    def connect_driver(self):
        self.driver = webdriver.Chrome(executable_path=constants.DRIVER_PATH)

    def get_bank_info(self, username: str, password: str) -> int:
        self.driver.get(constants.BANK_LINK)
        self.driver.find_element_by_css_selector(constants.BANK_USERNAME_SELECTOR).send_keys(username)
        self.driver.find_element_by_css_selector(constants.BANK_PASSWORD_SELECTOR).send_keys(password)
        self.driver.find_element_by_css_selector(constants.BANK_LOGIN_BTN_SELECTOR).click()
        time.sleep(10)
        res = requests.get(constants.BALANCE_PAGE_LINK)
        res.raise_for_status()
        print(res.text)
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select(constants.BANK_BALANCE_SELECTOR)
        print(elems)

