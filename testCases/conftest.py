from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# def pytest_configure(config):
#     config.metadata['Project Name'] = "nopCommerce"
#     config.metadata["Module Name"] = "Customer"
#     config.metadata["Tester"] = "Poresh"
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_Home", None)
#     metadata.pop("Plugins", None)
