from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """Locators"""
    MY_ACCOUNT_BUTTON = (By.ID, "menu-item-22")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    HELLO = (By.XPATH, "//h1[@class='entry-title']")
    ERROR = (By.XPATH, "//ul[@class='woocommerce-error']")

    def __init__(self, driver):
        """Constructor of the page class"""
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions for login page"""
    """used to login to an app"""

    def do_login(self, username, password):
        self.do_click(self.MY_ACCOUNT_BUTTON)
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def do_logout(self):
        self.do_click(self.MY_ACCOUNT_BUTTON)
        self.do_click(self.LOGOUT_BUTTON)

    def get_login_page_title(self, title):
        """Used to get the page title"""
        return self.get_title(title)

    def username_field(self):
        return self.is_visible(self.USERNAME)

    def my_account_text_is_visible(self):
        return self.is_visible(self.HELLO)

    def error_is_displayed(self):
        return self.is_visible(self.ERROR)
