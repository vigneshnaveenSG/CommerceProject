from Utility.ExcelUtils import ExcelUtils
from Utility.Logger import Logger
from Utility.configreader import readconfig
from Utility.frameworkutils import parse_Xml_files


class BaseTest():
    loging = Logger.log()
    xlutil = ExcelUtils()
    xldict = xlutil.readExcel()
    xml_file = readconfig("Mandatory", "Test_cases")
    test_cases = parse_Xml_files(xml_file)




