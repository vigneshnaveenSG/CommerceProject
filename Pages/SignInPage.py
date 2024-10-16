from seleniumpagefactory.Pagefactory import PageFactory
from Tests.BaseTest import BaseTest
from Utility.commonutils import commonutils


class SignInPage(PageFactory,BaseTest):


    def __init__(self, driver,testname):
        self.driver = driver
        self.testname = testname
        self.tcid = self.test_cases.get(self.testname)
        self.cu = commonutils()
        self.pageName = "SignIn"

    locators = {
           'txt_UserName': ('ID', "Email"),
           'txt_Password': ('ID', 'Password'),
           'txt_Login': ('XPATH', "//button[contains(text(),'Log in')]"),
           'img_Logo': ('CSS',"img.brand-image-xl"),
            'lnk_Catalog': ('XPATH', "(//p[contains(text(),'Catalog')])[1]"),
            'lnk_Products': ('XPATH', "(//p[contains(text(),'Products')])[1]"),
            'lnk_Categories': ('XPATH', "(//p[contains(text(),'Categories')])[1]"),
            'lnk_Manufacturers': ('XPATH', "(//p[contains(text(),'Manufacturers')])[1]"),
            'lnk_ProductReviews': ('XPATH', "(//p[contains(text(),'Product reviews')])"),
            'lnk_ProductTags': ('XPATH', "(//p[contains(text(),'Product tags')])"),
            'lnk_Attributes': ('XPATH', "(//p[contains(text(),'Attributes')])"),
            'img_Products_hdr': ('XPATH', "(//h1[contains(text(),'Products')])")
    }

    def Login(self):
        self.cu.enterTextbox(self.txt_UserName,self.tcid, self.pageName, "UserName")
        self.cu.enterTextbox(self.txt_Password, self.tcid, self.pageName, "Password")
        blnstatus = self.cu.clkButton( self.txt_Login, self.tcid, self.pageName, "Login Button")
        if blnstatus:
            self.loging.info("Login Button Clicked Successfully")
            blnstr = self.img_Logo.is_displayed()
            if blnstr:
                self.loging.info("Home Page is displayed")
