from ddt import ddt, data, unpack

from POM.AuthenticationContext.LoginLogoutPage import LoginLogoutPage
from POM.PropertyContext.FollowUpOrderPage import FollowUpOrdersPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class FollowUpOrder(BaseTestCase):

    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','Admin'))
    @unpack
    def test_FollowOrder_valid(self, username, password):
        LoginLogoutPage.login_with_valid_credentials(self, username, password)
        self.assertEqual('Payment pending',FollowUpOrdersPage.FollowOrder(self))

