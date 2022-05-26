from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage


class TestLogin(BaseTest):
    """This is testing class. Assert here"""

    def test_login_valid_creds(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME_VALID, TestData.PASSWORD_VALID)

        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

        my_account = self.loginPage.my_account_text_is_visible()
        assert my_account == TestData.MY_ACCOUNT_TEXT

    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()

        username_field = self.loginPage.username_field()
        assert username_field == TestData.USERNAME_FIELD

    def test_login_invalid_creds(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME_INVALID, TestData.PASSWORD_INVALID)

        error = self.loginPage.error_is_displayed()
        assert error == TestData.ERROR
