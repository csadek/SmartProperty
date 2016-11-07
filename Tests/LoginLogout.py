from Utilities.BaseTestCase import BaseTestCase
from POM.AuthenticationContext.LoginLogoutPage import LoginLogoutPage


class LoginLogout(BaseTestCase):

    def test_login(self):
        self.assertTrue(LoginLogoutPage.login(self))

    def test_logout(self):
        LoginLogoutPage.logout(self)