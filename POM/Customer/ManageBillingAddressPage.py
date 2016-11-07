from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from POM.Customer.CustomerBase import CustomerBase
from Utilities import ConfigReader as Conf


class ManageBillingAddressPage(CustomerBase):
    PageTitle = (By.CLASS_NAME,'page_title')
    BillingAddressLink = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div > div:nth-child(5) > div:nth-child(3) > a')
    billingAddressList = (By.NAME , 'personal_address_bill')
    shippingAddressList = (By.NAME,'personal_address_ship')

    #Create Another address Elements
    creatAddressBtn = (By.PARTIAL_LINK_TEXT ,'Create another address')
    surnameAddress=(By.NAME,'name_adresse')
    TypeList= (By.NAME, "address_type")   # type drop down list
    Surname = (By.ID, 'nom_famille')
    FirstName = (By.ID, 'prenom')
    Email = (By.ID,'email')
    Company = (By.ID, 'societe')
    Address = (By.ID, 'adresse')
    Zipcode = (By.ID, 'code_postal')
    Town = (By.ID, 'ville')
    Country = select_Country = (By.ID, "pays")
    Phone = (By.ID, 'portable')
    ValidateBtn = (By.CSS_SELECTOR ,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > form > fieldset > p > input' )
    createAddressMsg = (By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div.alert.alert-success.fade.in')

    def navigate_to_manage_billing(self):
        self.driver.get(Conf.read_ini_config('Paths','HomeURL'))
        self.driver.find_element(*ManageBillingAddressPage.BillingAddressLink).click()

    def Create_Another_Address(self,surAddress,surName,firstName,email,company,address,zipCode,town,country,phone):
        self.driver.find_element(*ManageBillingAddressPage.creatAddressBtn).click()
        self.driver.find_element(*ManageBillingAddressPage.surnameAddress).send_keys(surAddress)
        self.driver.find_element(*ManageBillingAddressPage.Surname).send_keys(surName)
        self.driver.find_element(*ManageBillingAddressPage.FirstName).send_keys(firstName)
        self.driver.find_element(*ManageBillingAddressPage.Email).send_keys(email)
        self.driver.find_element(*ManageBillingAddressPage.Company).send_keys(company)
        self.driver.find_element(*ManageBillingAddressPage.Address).send_keys(address)
        self.driver.find_element(*ManageBillingAddressPage.Zipcode).send_keys(zipCode)
        self.driver.find_element(*ManageBillingAddressPage.Town).send_keys(town)
        self.driver.find_element(*ManageBillingAddressPage.Country).send_keys(country)
        self.driver.find_element(*ManageBillingAddressPage.Phone).send_keys(phone)
        self.driver.find_element(*ManageBillingAddressPage.ValidateBtn).click()


    def get_surName_address(self):
        return self.driver.find_element(*ManageBillingAddressPage.surnameAddress).text

    def get_createAddress_msg(self):
        return self.driver.find_element(*ManageBillingAddressPage.createAddressMsg).text

    def get_billingAddress_list(self):
        no = Select( self.driver.find_element(*ManageBillingAddressPage.billingAddressList))
        return no

    def get_shippingAddress_list(self):
        listno= Select( self.driver.find_element(*ManageBillingAddressPage.shippingAddressList))
        return listno
