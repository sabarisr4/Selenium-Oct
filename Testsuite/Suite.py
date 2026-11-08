
import unittest
from HtmlTestRunner import HTMLTestRunner

from Testsuite.F1 import First
from Testsuite.F2 import Two
from Testsuite.F3 import Three

# from packagename.filename import class name



# step2 : collect test cases from classes
# TestLoader class => unittest



t1=unittest.TestLoader().loadTestsFromTestCase(First)
t2=unittest.TestLoader().loadTestsFromTestCase(Two)
t3=unittest.TestLoader().loadTestsFromTestCase(Three)

# step3: creating a test suite

demo=unittest.TestSuite([t1,t2,t3])

if __name__=='__main__':
    unittest.main(testRunner=HTMLTestRunner(open_in_browser=True, output='testsuite.html'))
#testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports\\dhivya.html
#unittest.main(testRunner=HTMLTestRunner(title="first",open_in_browser=True,description="first report",output='sabari.html'))