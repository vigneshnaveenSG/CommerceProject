from seleniumpagefactory import PageFactory
from Tests.BaseTest import BaseTest
from Utility.commonutils import commonutils



class AddNewProductPage(PageFactory,BaseTest):

    def __init__(self, driver,testname):
        self.driver = driver
        self.testname= testname
        self.tcid = self.test_cases.get(self.testname)
        self.cu = commonutils()
        self.pageName = "AddNewProduct"


    locators = {
        'img_AddnewProduct': ('xpath', "//h1[contains(text(),'Add a new product')]"),
        'txt_Productname': ('id', "Name"),
        'btn_save': ('name', "save")
        }

    def addnewproducts(self):
        if self.img_AddnewProduct.is_displayed():
            self.cu.enterTextbox(self.txt_Productname, self.tcid, self.pageName, "ProductName")
            self.cu.clkButton(self.btn_save, self.tcid, self.pageName, "Save Button")
