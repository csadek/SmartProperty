from selenium.webdriver.common.by import By

from Utilities import ConfigReader as Conf
from Utilities.BaseTestCase import BaseTestCase


class LoginLogoutPage(BaseTestCase):
    """ this class represent login page elements manipulations and functions"""
    # Navigator
    login_link = (By.CLASS_NAME,'header_user_text')
    admin_url = Conf.read_ini_config('Paths','AdminURL')
    home_url = Conf.read_ini_config('Paths','HomeURL')

    # Locators
    username = (By.NAME,'email')
    password =(By.NAME,'mot_passe')
    login_button = (By.CSS_SELECTOR,'input[class="btn btn-success"')
    Error_LBL = (By.CSS_SELECTOR, 'div[class="alert alert-danger fade in"]')
    # logout
    log_out_admin = (By.CSS_SELECTOR, 'span[class ="glyphicon glyphicon-off"')
    logout_link = (By.CSS_SELECTOR,'#header_login > div > a > span.hidden-xs > span.header_user_text')
    logout_user = (By.LINK_TEXT,'Log out')

    """ Use login method to login either with valid, invalid or blank credentials. Also, if used when the user is
    logged in it will not try to re-login"""
    def login(self, username, password):
        if LoginLogoutPage.admin_url in self.driver.current_url:
            self.driver.get(*LoginLogoutPage.home_url)
        if self.driver.find_element(*LoginLogoutPage.login_link).text == 'Log in':
            self.driver.find_element(*LoginLogoutPage.login_link).click()
            self.driver.find_element(*LoginLogoutPage.username).clear()
            self.driver.find_element(*LoginLogoutPage.username).send_keys(username)
            self.driver.find_element(*LoginLogoutPage.password).clear()
            self.driver.find_element(*LoginLogoutPage.password).send_keys(password)
            self.driver.find_element(*LoginLogoutPage.login_button).click()
            user_mail =  self.driver.find_element(*LoginLogoutPage.login_link).text
            if user_mail == 'Log in':
                return self.driver.find_element(*LoginLogoutPage.Error_LBL)
            else:
                return user_mail

    """ logout method will log you out either if you are at customer or admin view .Also, if used when the user is
    logged out it will not try to re-log out"""
    def logout(self):
        if LoginLogoutPage.admin_url in self.driver.current_url:
            self.driver.find_element(*LoginLogoutPage.log_out_admin).click()
        elif self.driver.find_element(*LoginLogoutPage.logout_link).text != 'Log in':
            self.driver.find_element(*LoginLogoutPage.logout_link).click()
            self.driver.find_element(*LoginLogoutPage.logout_user).click()
