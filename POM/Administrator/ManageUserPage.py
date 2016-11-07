from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase


class ManageUserPage(AdminBase):
    """ this class represents manage users page elements manipulations and functions"""
    """give user admin permission to be able to view all products"""
    # Locators
    users_mail = (By.CSS_SELECTOR,'#tablesForm > tbody > tr > td:nth-child(3) > a')
    user_permission = (By.CSS_SELECTOR,'select[name="priv[]"] option')
    save_button = (By.CSS_SELECTOR,'input[class="btn btn-primary"')
    alert =(By.CSS_SELECTOR,'div[class="alert alert-success fade in"] b')

    # Edit user privileges
    def edit_user(self,username,password,email):
        # Open edit user page
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.view_users(self)
        # click on edit for specific user
        for user in self.driver.find_elements(*ManageUserPage.users_mail):
            if user.text == email:
                ref = user.get_attribute('href')
                user_id=ref.split('=')
                id = user_id[1]
                self.driver.find_element_by_css_selector('a[href="http://10.1.22.67/Jamaica/administrer/utilisateurs.php?mode=modif&id_utilisateur={}&start=0"]'.format(id)).click()
                # change permission
                for x in self.driver.find_elements(*ManageUserPage.user_permission):
                    if x.text != '[Jamaica] Client':
                        x.click()
                self.driver.find_element(*ManageUserPage.save_button).click()
                return self.driver.find_element(*ManageUserPage.alert).text
            else:
                continue