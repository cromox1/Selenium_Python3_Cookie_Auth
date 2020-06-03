__author__ = 'cromox'

import pytest
import sys
from base.webdriverfactory import WebDriverFactory as webbrowser

@pytest.yield_fixture()
def setUp():
    print("\n--- > Running method level setUp")
    yield
    print("\n--- > Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, mainURL="https://www.google.co.uk"):

    print("\n== > Running one time setUp")
    print('Python Version = ' + sys.version)

    wdf = webbrowser(browser)
    driver = wdf.getWebDriverInstance(mainURL)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\n== > Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")