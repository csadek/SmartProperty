from ddt import ddt, data, unpack

from POM.Administrator.ManageUserPage import ManageUserPage
from POM.NewUser.RegestrationPage import RegistrationPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class OpenAccount(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Admin']))
    @unpack
    def test_OpenAccount(self,admin,adminpass,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website, confirm):
        self.assertIn(confirm,RegistrationPage.Register_with_valid_input(self,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website))
        self.assertTrue(RegistrationPage.mail,RegistrationPage.verify_user_at_DB(self))
        self.assertIn(RegistrationPage.mail,ManageUserPage.edit_user(self,admin,adminpass,RegistrationPage.mail))


