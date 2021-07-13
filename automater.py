import constants
from selenium import webdriver
import time


class Connector:
    def connect_driver(self):
        self.driver = webdriver.Chrome(executable_path=constants.DRIVER_PATH)

    def get_bank_info(self) -> int:
        self.driver.get('https://login.bankhapoalim.co.il/ng-portals/auth/en/')
        time.sleep(3)
        return 0
