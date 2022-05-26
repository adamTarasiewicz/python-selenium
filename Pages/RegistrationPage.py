from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class RegistrationPage(BasePage):
    """finding elements By locators"""
    MY_ACCOUNT_BUTTON = (By.ID, "menu-item-22")
    USERNAME = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.NAME, "register")
    HELLO = (By.XPATH, "//h1[@class='entry-title']")

    def __init__(self, driver):
        """Constructor of the page class"""
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions for registration"""
    """this is used to register new account on the website"""

    def do_register(self, username, password):
        self.do_click(self.MY_ACCOUNT_BUTTON)
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.REGISTER_BUTTON)

    def my_account_text_is_visible(self):
        return self.is_visible(self.HELLO)
