import os

from Utility.configreader import readconfig
import pytest
import sys
import pytest_html
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
sys.path.append("//")


@pytest.fixture()
def setup_teardown(request):
    global driver,testname
    driver=launch_browser()
    request.cls.driver = driver
    testname = os.path.basename(request.node.fspath)
    test_folder = os.path.basename(os.path.dirname(request.node.fspath))
    print("Test Folder"+test_folder)
    request.cls.testname = test_folder+"/"+testname
    yield
    driver.quit()

def launch_browser():
    browser = readconfig("Mandatory", "browser")
    print(browser)
    if browser.__eq__("chrome"):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
    elif browser.__eq__("firefox"):
        driver = webdriver.firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    url = readconfig("Mandatory", "url")
    print(url)
    driver.get(url)
    driver.implicitly_wait(100)
    return driver


def pytest_html_report_title(report):
    report.title = "This is the Commerce Project Report"


def pytest_configure(config):
    config.stash[metadata_key]["Environment"] = "QA"


def test_extra(extras):
    extras.append(pytest_html.extras.text("some string added by me"))


def capture_screenshot(name):
    driver.get_screenshot_as_file(name)


def pytest_html_results_table_header(cells):
    cells.insert(6, "<th>Expected Result</th>")
    cells.insert(5, '<th>Actual Result</th>')
    cells.insert(4, '<th>Description</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(4, '<td>Product Creation</td>')
    cells.insert(5, '<td>New Product should be created</td>')
    cells.insert(6, '<td>New Product has created successfully</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extras = getattr(report, "extras", [])
    print("Entered the maker report")
    if report.when == "call" or report.when == "setup":
        print("Entered the Loop")
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            filename = report.nodeid.replace("::", "-") + ".png"
            print(filename)
            htm=('<html><Table><TH>Step Number</TH><TH>Description</TH><TH>Expected Result</TH><TH>Actual Result</TH></Table></html>')
            capture_screenshot(filename)
            extras.append(pytest_html.extras.html(htm))
            if filename:
                html = ('<div>src="%s" alt="screenshot" style="width:304px;height:228px;" ' 
                        'onclick="window.open(this.src)" align="right"</div>') % filename
                extras.append(pytest_html.extras.html(html))
    report.extras = extras
