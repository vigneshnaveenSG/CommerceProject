from Tests.conftest import setup_teardown
from Pages.SignInPage import SignInPage
import pytest

from Tests.BaseTest import BaseTest


@pytest.mark.usefixtures("setup_teardown")
class Test_signIn(BaseTest):

    def test_login(self):
        SignIn = SignInPage(self.driver)
        SignIn.set_username()
        self.loging.info("Username is set")
        SignIn.set_password()
        self.loging.info("Password is set")
        SignIn.click_login()
        self.loging.info("Login Page is displayed")
