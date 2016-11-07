import os
import sys
sys.path.append(os.path.abspath(os.path.join(sys.path[0], os.pardir)))
from Utilities.BaseTestCase import BaseTestCase
from POM.LoginLogoutPage import LoginLogoutPage
from POM.NewUser.RegestrationPage import RegistrationPage
from POM.Administrator.ManageUserPage import ManageUserPage
from POM.Customer.ManageBillingAddressPage import ManageBillingAddressPage
from POM.Customer.searchPage import SearchPage
from POM.Customer.PaymentPages import PaymentPages
from POM.Customer.FollowUpOrderPage import FollowUpOrdersPage
from Utilities.ReadExcel import ReadExcel
from ddt import ddt, data, unpack


@ddt
class Smoke(BaseTestCase):

    @unpack
    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Registration']))
    def test_smoke_testcase1(self,admin,adminpass,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website, confirm):
        self.assertIn(confirm,RegistrationPage.Register_with_valid_input(self,password,firstName,surname,company,capacity,dateofbirth,phone,mobile,address,zipcode,town,country,how_do_you_know_our_website))
        self.assertTrue(RegistrationPage.mail,RegistrationPage.verify_user_at_DB(self))
        self.assertIn(RegistrationPage.mail,ManageUserPage.edit_user(self,admin,adminpass,RegistrationPage.mail))
        LoginLogoutPage.logout(self)
        self.assertEqual(RegistrationPage.mail,LoginLogoutPage.login(self,RegistrationPage.username,password))

    @unpack
    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Products','ShppingAddress']))
    def test_smoke_testcase2(self,productName,Category,surAddress, surName, firstName, email, company, address, zipCode,
                                                town, country, phone):
        ManageBillingAddressPage.navigate_to_manage_billing(self)
        old_billing_no = len(ManageBillingAddressPage.get_billingAddress_list(self).options)
        ManageBillingAddressPage.Create_Another_Address(self, surAddress, surName, firstName, email, company, address,
                                                        zipCode, town, country, phone)

        # assert that the new address is created and added to drop down list
        self.assertIn('Your new address was created.', ManageBillingAddressPage.get_createAddress_msg(self))
        self.assertEqual(old_billing_no+1, len(ManageBillingAddressPage.get_billingAddress_list(self).options))
        self.assertEqual(old_billing_no+1 , len(ManageBillingAddressPage.get_shippingAddress_list(self).options))

        # Make the added address is default billing and shipping address
        ManageBillingAddressPage.get_billingAddress_list(self).select_by_visible_text(surAddress)
        ManageBillingAddressPage.get_shippingAddress_list(self).select_by_visible_text(surAddress)
        SearchPage.search_data(self,productName,Category)
        self.assertIn('Confirmation of your order',PaymentPages.pay_product(self,'grey','Large','2'))
        self.driver.get_screenshot_as_file('screenshot_PayConfirm.jpg')
        self.assertEqual('Payment pending',FollowUpOrdersPage.FollowOrder(self))