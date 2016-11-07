from selenium.webdriver.common.by import By

from POM.Customer.CustomerBase import CustomerBase
from Utilities import ConfigReader as Conf


class FollowUpOrdersPage(CustomerBase):
    """ this class represent FollowUp_Orders page elements manipulations and functions"""
    # Locators
    FollowUp_Orders_Lnk = (By.LINK_TEXT, 'Follow-up of orders')
    FollowUp_Orders_Title = (By.CLASS_NAME,'liste_commandes')
    PaymentStatus_Lnk = (By.LINK_TEXT, 'Payment pending')
    OrderNumber = (By.CSS_SELECTOR, 'div.middle_column_repeat > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')

    def FollowOrder(self):
        self.driver.get(Conf.read_ini_config('Paths','HomeURL'))
        self.driver.find_element(*FollowUpOrdersPage.FollowUp_Orders_Lnk).click()
        self.driver.implicitly_wait(10)
        status =self.driver.find_element(*FollowUpOrdersPage.PaymentStatus_Lnk).text
        self.driver.find_element(*FollowUpOrdersPage.PaymentStatus_Lnk).click()
        return status






