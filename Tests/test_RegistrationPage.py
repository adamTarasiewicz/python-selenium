from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.RegistrationPage import RegistrationPage


class TestRegistration(BaseTest):
    """RUN THIS ONLY ONCE, and only with one browser defined in [conftest.py] for account creation"""
    """Accounts last for 24 hours on seleniumdemo.com"""

    # Account creation
    def test_registration(self):
        self.registrationPage = RegistrationPage(self.driver)
        self.registrationPage.do_register(TestData.USER_NAME_VALID, TestData.PASSWORD_VALID)
        my_account = self.registrationPage.my_account_text_is_visible()
        assert my_account == TestData.MY_ACCOUNT_TEXT
