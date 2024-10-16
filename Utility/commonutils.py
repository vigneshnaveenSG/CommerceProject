import time

from Tests.BaseTest import BaseTest
class commonutils(BaseTest):

    def enterTextbox(self,objName, TCId, pgeName, colName):
        tstData = self.xlutil.readTestData(self.xldict, TCId, pgeName, colName)
        objName.clear()
        objName.set_text(tstData)
        self.loging.info("The Value "+tstData+" was entered in textbox "+colName+" Successfully")

    def clkButton(self,objName, TCId, pgeName, colName):
        objName.click()
        time.sleep(20)
        self.loging.info("The "+ colName+ " clicked successfully")
        return True

