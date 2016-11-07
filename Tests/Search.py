from ddt import ddt, data, unpack

from POM.Customer.searchPage import SearchPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class Search(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Search']))
    @unpack
    def test_search(self,username,password,scen,productName,Category,result):
        LoginLogoutPage.login(self, username, password)
        self.assertIn(result,SearchPage.search_data(self,productName,Category))





