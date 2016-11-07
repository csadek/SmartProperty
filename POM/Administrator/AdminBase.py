from selenium.webdriver.common.by import By
from POM.LoginLogoutPage import LoginLogoutPage
from Utilities import ConfigReader as Conf
from Utilities.BaseTestCase import BaseTestCase


class AdminBase(BaseTestCase):
    # Navigators
    admin_button = (By.CSS_SELECTOR,'a[class="btn btn-warning pull-right"]')
    products_main =(By.CSS_SELECTOR, '#menu_label_products')
    products_sub =(By.CSS_SELECTOR, '#menu_1bd8d94f')
    product_list_link=(By.CSS_SELECTOR,'a[title="Products list"]')
    add_product_link = (By.CSS_SELECTOR,'a[title="Add a product"]')
    category_sub = (By.CSS_SELECTOR, '#menu_820845ea')
    add_category_link = (By.CSS_SELECTOR,'a[title="Add category"]')
    category_list_link = (By.CSS_SELECTOR,'a[title="Categories list"]')
    users_main =(By.CSS_SELECTOR, '#menu_label_users')
    users_sub = (By.CSS_SELECTOR, '#menu_3233bb4a')
    users_list_link = (By.CSS_SELECTOR,'a[title="Users list"]')
    customer_loyalty_link = (By.CSS_SELECTOR, '#menu_bc24ec8e')
    coupon_codes_link = (By.CSS_SELECTOR,'a[title="Coupon codes"]')

    # navigate to admin pages
    def navigate_to_admin(self,username, password):
        if Conf.read_ini_config('Paths','HomeURL') in self.driver.current_url:
            self.driver.find_element(*AdminBase.admin_button).click()
        elif Conf.read_ini_config('Paths','AdminURL') not in self.driver.current_url:
            if self.driver.find_element(*LoginLogoutPage.login_link).text == 'Log in':
                LoginLogoutPage.login(self,username,password)
                self.driver.get(Conf.read_ini_config('Paths','HomeURL'))
                self.driver.find_element(*AdminBase.admin_button).click()

    def view_users(self):
        self.driver.find_element(*AdminBase.users_main).click()
        self.driver.find_element(*AdminBase.users_sub).click()
        self.driver.find_element(*AdminBase.users_list_link).click()

    def add_coupon_navigator(self):
        self.driver.find_element(*AdminBase.users_main).click()
        self.driver.find_element(*AdminBase.customer_loyalty_link).click()
        self.driver.find_element(*AdminBase.coupon_codes_link).click()

    def edit_product_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.products_sub).click()
        self.driver.find_element(*AdminBase.product_list_link).click()

    def add_product_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.products_sub).click()
        self.driver.find_element(*AdminBase.add_product_link).click()

    def edit_category_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.category_sub).click()
        self.driver.find_element(*AdminBase.category_list_link).click()

    def add_category_navigator(self):
        self.driver.find_element(*AdminBase.products_main).click()
        self.driver.find_element(*AdminBase.category_sub).click()
        self.driver.find_element(*AdminBase.add_category_link).click()

