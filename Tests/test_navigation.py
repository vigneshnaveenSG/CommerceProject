from Tests.conftest import setup_teardown
from Pages.navigationpage import navigationpage
from Pages.SignInPage import SignInPage
import pytest

from Tests.BaseTest import BaseTest


@pytest.mark.usefixtures("setup_teardown")
class Test_navigation(BaseTest):

    def test_navigation(self):
        SignIn = SignInPage(self.driver,self.testname)
        SignIn.Login()
        nav=navigationpage(self.driver,self.testname)

        nav.nav_products()
        self.loging.info("Navigated to Product Screen Successfully")
        nav.nav_producttags()
        self.loging.info("Navigated to Product Tags  Screen Successfully")
        nav.nav_productreviews()
        self.loging.info("Navigated to Product Reviews  Screen Successfully")
        nav.nav_categories()
        self.loging.info("Navigated to Categories  Screen Successfully")
        nav.nav_manufacturers()
        self.loging.info("Navigated to Manufacturers  Screen Successfully")
