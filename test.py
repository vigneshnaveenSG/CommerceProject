import xml.etree.ElementTree as ET
import pytest
import subprocess

from Utility.frameworkutils import parse_Xml_files


#from Utility.frameworkutils import parse_Xml_files

def run_pytest_with_tests(test_cases):
    pytest_args = "pytest -v -s --html=Reports/report.html --self-contained-html"
    # Construct the pytest command with the selected test cases
    for i in range(len(test_cases)):
        pytest_args=pytest_args +" "+ test_cases[i]
    result = subprocess.run(pytest_args)

  #  result = subprocess.run('pytest -v -s --html=Reports/report.html --self-contained-html Tests/test_products.py Tests/test_SignIn.py')
    return result.returncode


if __name__ == "__main__":
    # Path to your XML file
    xml_file = 'testcases.xml'


    # Parse test names from XML
    test_cases = parse_Xml_files(xml_file)
    if test_cases:
        # Run pytest with extracted test cases
        return_code = run_pytest_with_tests(list(test_cases.keys()))
        if return_code == 0:
            print("All tests passed!")
        else:
            print("Some tests failed.")
    else:
        print("No test cases found.")