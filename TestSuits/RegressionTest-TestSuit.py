import unittest
import datetime as dt
import os
import sys
from Utilities import HTMLTestRunner
from Tests.LoginLogout import LoginLogout


# navigate to the relative paths from the batch file
sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))

# create the html report file
current_directory = (os.path.dirname(os.getcwd()))
outfile = open(current_directory + '\Reports\TestReport_' + dt.datetime.now().strftime("%Y-%m-%d_%H%M%S"+ ".html"), "w")

# get all tests for the system test
login_tests = unittest.TestLoader().loadTestsFromTestCase(LoginLogout)

#   Creating a Test Suite using the imported Test Case Files
test_full = unittest.TestSuite([login_tests])

runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Test Suite Report'
)

# run the suite using HTMLTEstRunner
runner.run(test_full)