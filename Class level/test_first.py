import pytest
import logging


#create the class
#create the testcase


@pytest.mark.usefixtures("setup")
class TestExampleOne:

    def test_max(self):
        logging.debug("Maximizing browser window")
        self.driver.maximize_window()