import pytest
from Tests.conftest import setup_teardown
from Pages.AddNewProductPage import AddNewProductPage
from Pages.ProductsPage import productspage
from Pages.SignInPage import SignInPage
from Pages.navigationpage import navigationpage
from Tests.BaseTest import BaseTest


@pytest.mark.usefixtures("setup_teardown")
class Test_products(BaseTest):

    def test_products(self):

        signin = SignInPage(self.driver,self.testname)
        signin.Login()
        self.loging.info("Login Completed Successfully")

        nav = navigationpage(self.driver,self.testname)
        nav.nav_products()
        self.loging.info("Product Screen Navigation completed Successfully")

        prod = productspage(self.driver,self.testname)
        prod.click_addnew()
        self.loging.info("Add Products Screen Navigation completed Successfully")

        addnew = AddNewProductPage(self.driver,self.testname)
        addnew.addnewproducts()
        self.loging.info("New product added  Successfully")