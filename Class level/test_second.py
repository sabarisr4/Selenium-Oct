import pytest
import logging

from selenium.webdriver.common.by import By

#create the class
#create the testcase

@pytest.mark.usefixtures("setup")
class Testexampletwo:

    def test_refresh(self):
        logging.debug("Going to refresh the screen")
        self.driver.refresh()

    def test_click(self):
        logging.warning("Clicking Images link")

        self.driver.find_element(By.LINK_TEXT,"Images").click()

        self.driver.save_screenshot("class level.png")


#conftest.py(before yield)   class1:maximize testcase  conftest.py(after yield)

#conftest.(before yield)   class2:test case 2   conftest.py(after yield)

#Run = py.test -v -s --html=class fix.html --capture=sys




"""
pytest

pytest install
pytest html
pytest ordering
pytest dependency
test_
file name test_
class name test_
normal file
normal file with verbosity
normal file with bring statement
filtering:keyword
filtering:marking
and or
report generation
test suites run
pytest fixtures
class level
function level
"""