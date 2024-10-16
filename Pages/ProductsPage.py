from seleniumpagefactory import PageFactory

from Tests.BaseTest import BaseTest
from Utility.commonutils import commonutils


class productspage(PageFactory,BaseTest):

    def __init__(self, driver, testname):
        self.driver = driver
        self.testname = testname
        self.tcid = self.test_cases.get(self.testname)
        self.cu = commonutils()
        self.pageName = "Products"

    locators = {
        'btn_Addnew': ('xpath', "//a[contains(@href,'Create')]"),
        'btn_dwnldCatalog': ('name', "download-catalog-pdf"),
        'btn_import': ('name', "importexcel"),
        'btn_delete': ('id', "delete-selected")
        }

    def click_addnew(self):

        if self.btn_Addnew.is_displayed():
            self.cu.clkButton(self.btn_Addnew, self.tcid, self.pageName, "Add new Button")

    def click_dwncatalog(self):
        if self.btn_dwnldCatalog.is_displayed():
            self.cu.clkButton(self.btn_dwnldCatalog, self.tcid, self.pageName, "Download Catalog Button")


    def click_import(self):
        if self.btn_import.is_displayed():
            self.cu.clkButton(self.btn_import, self.tcid, self.pageName, "Import Button")


    def click_delete(self):
        if self.btn_delete.is_displayed():
            self.cu.clkButton(self.btn_delete, self.tcid, self.pageName, "Delete Button")