from ddt import ddt, data, unpack

from POM.AuthenticationContext.LoginLogoutPage import LoginLogoutPage
from POM.PropertyContext.PaymentPages import PaymentPages
from POM.PropertyContext.searchPage import SearchPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class Payment(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Products']))
    @unpack
    def test_payment(self,userName,password,productName,Category):
        LoginLogoutPage.login_with_valid_credentials(self,userName,password)
        SearchPage.search_data(self,productName,Category)
        self.assertIn('Confirmation of your order',PaymentPages.pay_product(self,'grey','Large','2'))
        self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')
