from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase
from POM.Customer.CustomerBase import CustomerBase



class ProductDetailsPage(CustomerBase):
    """ this class represent login page elements manipulations and functions"""
    # Locators
    sendEmailLink = (By.PARTIAL_LINK_TEXT,'Send email to your friend')
    addToNotePad = (By.PARTIAL_LINK_TEXT,'Add to notepad')
    productInfo = (By.PARTIAL_LINK_TEXT,'Product Info')
    zoomTool = (By.CLASS_NAME,'zoomPup')

    # Details tabs
    availability= (By.PARTIAL_LINK_TEXT,'Availability')
    washingTab = (By.PARTIAL_LINK_TEXT,'Washing')

    #Add to notepad
    MyAccountLink=(By.PARTIAL_LINK_TEXT,'My Account')
    myReminder= (By.PARTIAL_LINK_TEXT,'Check my reminder')
    table=(By.CLASS_NAME,'table-responsive')
    reminder_name = (By.CSS_SELECTOR,'#main_content > div > div > div > div.middle_column_repeat > div > table > tbody > tr > td.lignecaddie_produit_details > a')

    #Give your opinion Link
    opinionLink= (By.PARTIAL_LINK_TEXT,'Give your opinion')
    yourOpinionText=(By.NAME,'avis')
    sendOpinionBtn=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > form > table > tbody > tr:nth-child(7) > td > input')
    rate= (By.NAME,'note')
    confirmMsg=(By.CSS_SELECTOR,'#main_content > div:nth-child(1) > div > div > div.middle_column_repeat > div.alert.alert-success.fade.in')


    def get_product_details(self,ProductName):
        self.driver.find_element_by_partial_link_text(ProductName).click()

    def ge_details_tab(self):
        self.driver.find_element(*ProductDetailsPage.availability).click()
        self.driver.find_element(*ProductDetailsPage.washingTab).click()

    def zoom_product_image(self):
         element=self.driver.find_element(*ProductDetailsPage.zoomTool)
         self.driver.implicitly_wait(30)

    def send_email(self):
        self.driver.find_element(*ProductDetailsPage.sendEmailLink).click()

    def give_your_Opinion_page(self,Opinion):
         self.driver.find_element(*ProductDetailsPage.opinionLink).click()
         self.driver.find_element(*ProductDetailsPage.yourOpinionText).send_keys(Opinion)
         self.driver.find_element(*ProductDetailsPage.rate).click()
         self.driver.find_element(*ProductDetailsPage.sendOpinionBtn).click()

    def add_to_notePad_Page(self,product_name):
        self.driver.find_element(*ProductDetailsPage.addToNotePad).click()
        self.driver.find_element(*ProductDetailsPage.MyAccountLink).click()
        self.driver.find_element(*ProductDetailsPage.myReminder).click()
        for i in self.driver.find_elements(*ProductDetailsPage.reminder_name):
            if i.text == product_name:
                return True
            else:
                return False









