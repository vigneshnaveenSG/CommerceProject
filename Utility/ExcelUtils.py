import pytest
import pandas as pd

from Utility import configreader
from Utility.configreader import readconfig


class ExcelUtils():

    def readExcel(self):
        df = pd.ExcelFile("C:/Learning/CommerceProject/TestData/TestData_COP.xlsx")
        xl_dict={}
        sheet_names=df.sheet_names
        for sheet_name in sheet_names:
            xl_dict[sheet_name]=df.parse(sheet_name)
        return xl_dict

    def readTestData(self,xldict, TcId, Sheet_name, Col_Name):
        datFrm = xldict.get(Sheet_name)
        filt = (datFrm['TestCaseId'] == TcId)
        prdname = datFrm.loc[filt,Col_Name].to_string(index=False)
        return prdname