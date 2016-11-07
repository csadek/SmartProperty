import os
import sys
sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))
from Utilities.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class LoginLogout(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','Login'))
    def test_login(self,scenario,username,password,msg):
        self.assertTrue(msg,LoginLogoutPage.login(self, username,password))

    def test_logout(self):
        LoginLogoutPage.logout(self)