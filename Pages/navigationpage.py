from seleniumpagefactory.Pagefactory import PageFactory
from Tests.BaseTest import BaseTest
from Utility.commonutils import commonutils


class navigationpage(PageFactory,BaseTest):

    def __init__(self, driver,testname):
        self.driver = driver
        self.testname = testname
        print("Navigation Page Test Name" + self.testname)
        self.tcid = self.test_cases.get(self.testname)
        print("Navigation Page Test case id"+self.tcid)
        self.cu = commonutils()
        self.pageName = "NavigationPage"

    locators = {
        'lnk_Catalog': ('XPATH', "(//p[contains(text(),'Catalog')])[1]"),
        'lnk_Products': ('XPATH', "(//p[contains(text(),'Products')])[1]"),
        'lnk_Categories': ('XPATH', "(//p[contains(text(),'Categories')])[1]"),
        'lnk_Manufacturers': ('XPATH', "(//p[contains(text(),'Manufacturers')])[1]"),
        'lnk_ProductReviews': ('XPATH', "(//p[contains(text(),'Product reviews')])"),
        'lnk_ProductTags': ('XPATH', "(//p[contains(text(),'Product tags')])"),
        'lnk_Attributes': ('XPATH', "(//p[contains(text(),'Attributes')])"),
        'img_Products_hdr': ('XPATH', "(//h1[contains(text(),'Products')])"),
        'img_Categories_hdr': ('XPATH', "(//h1[contains(text(),'Categories')])"),
        'img_Manufacturers_hdr': ('XPATH', "(//h1[contains(text(),'Manufacturers')])"),
        'img_Productreviews_hdr': ('XPATH', "(//h1[contains(text(),'Product reviews')])"),
        'img_Producttags_hdr': ('XPATH', "(//h1[contains(text(),'Product tags')])")

    }
        
    def nav_products(self):
        if self.lnk_Catalog.is_displayed():
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")
            self.cu.clkButton(self.lnk_Products, self.tcid, self.pageName, "Products Link")
        blnstr = self.img_Products_hdr.is_displayed()
        if blnstr:
            self.loging.info("Product Page is displayed")
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")

    def nav_categories(self):
        if self.lnk_Catalog.is_displayed():
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")
            self.cu.clkButton(self.lnk_Categories, self.tcid, self.pageName, "Categories Link")
        blnstr = self.img_Categories_hdr.is_displayed()
        if blnstr:
            self.loging.info("Categories Page is displayed")
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")

    def nav_manufacturers(self):
        if self.lnk_Catalog.is_displayed():
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")
            self.cu.clkButton(self.lnk_Manufacturers, self.tcid, self.pageName, "Manufacture Link")
        blnstr = self.img_Manufacturers_hdr.is_displayed()
        if blnstr:
            self.loging.info("Manufacurers Page is displayed")
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")

    def nav_productreviews(self):
        if self.lnk_Catalog.is_displayed():
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")
            self.cu.clkButton(self.lnk_ProductReviews, self.tcid, self.pageName, "Product Review Link")
        blnstr = self.img_Productreviews_hdr.is_displayed()
        if blnstr:
            self.loging.info("product Reviews Page is displayed")
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")

    def nav_producttags(self):
        if self.lnk_Catalog.is_displayed():
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")
            self.cu.clkButton(self.lnk_ProductTags, self.tcid, self.pageName, "Product Tag Link")
        blnstr = self.img_Producttags_hdr.is_displayed()
        if blnstr:
            self.loging.info("products Tags Page is displayed")
            self.cu.clkButton(self.lnk_Catalog, self.tcid, self.pageName, "Catalog Link")