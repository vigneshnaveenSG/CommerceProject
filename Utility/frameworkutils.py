import os
import xml.etree.ElementTree as ET

def parse_Xml_files(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    test_cases = {}
    for testcase in root.findall('testcase'):
        testname = testcase.get('Testname')
        testcaseid = testcase.get('TestCaseId')
        test_cases.update({testname:testcaseid})
    print(test_cases)
    #print(type(test_cases.keys()))
    print(list(test_cases.keys()))
    return test_cases