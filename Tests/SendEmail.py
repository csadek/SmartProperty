from ddt import ddt, data, unpack

from POM.Customer.ProductDetailsPage import ProductDetailsPage
from POM.Customer.SendEmailPage import SendEmailClass
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class sendEmailTestCases(BaseTestCase):

    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','Admin'))
    @unpack
    def test_add(self,user,password):
        LoginLogoutPage.login(self, user, password)

    @data(*ReadExcel.get_sheet('../Utilities/Data.xlsx','SendEmail'))
    @unpack
    def test_send_email_successfully(self,SenderName,SenderEmail,RecName,RecEmails,comment):
        ProductDetailsPage.get_product_details(self,'trouser')
        ProductDetailsPage.send_email(self)

        conformation_Msg = SendEmailClass.send_Email_successfully(self,SenderName,SenderEmail,RecName,RecEmails,comment)
        self.assertTrue('Your message has been sent.',conformation_Msg)
        SendEmailClass.back_to_product_Page(self)

    def test_send_empty_data(self):
     ProductDetailsPage.send_email(self)
     errorMessage = 'The form content is invalid (unvalid email ou missing data). Please click "back" and fill the forms with correct answers.'
     self.assertTrue(errorMessage ,SendEmailClass.send_Email_empty_data(self))


    def test_Open_Outlook(self):
        SendEmailClass.open_outlook(self,'jmohamed@integrant.com','Gaso3113')










