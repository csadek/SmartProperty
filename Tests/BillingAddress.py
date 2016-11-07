from ddt import ddt, data, unpack

from POM.Customer.ManageBillingAddressPage import ManageBillingAddressPage
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class MangeBilling(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','ShppingAddress']))
    @unpack
    def test_manage_billing(self,name,password,surAddress, surName, firstName, email, company, address, zipCode,
                                                town, country, phone):
        LoginLogoutPage.login_with_valid_credentials(self,name,password)
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


