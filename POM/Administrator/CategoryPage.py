from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase


class CategoryPage(AdminBase):
    """ this class represents add and delete both category and subcategory elements manipulations and functions"""
    """ Admin user should add categories and subcategories to add products to those categories """
    # Locators
    root_category = (By.CSS_SELECTOR, 'option[value="0"]')
    view_on_home = (By.NAME, 'on_special')
    state_online = (By.NAME, 'etat')
    name = (By.NAME, 'nom_en')
    parents = (By.CSS_SELECTOR, 'option[value]')
    add_category_button = (By.CSS_SELECTOR,'input[value="Add this category"]')

    # alert
    alert = (By.CSS_SELECTOR, 'div[class="alert alert-success fade in"]')

    # category online
    view_online = (By.CSS_SELECTOR, 'td a')
    page_title = (By.CSS_SELECTOR, 'h1[class="products_list_brief"]')

    # delete category
    confirm_delete = (By.CSS_SELECTOR,'button[class="btn btn-primary"]')

    # Add category or sub category
    def add_category(self,username,password,categoryname, parent):
        # Open category page
        AdminBase.navigate_to_admin(self,username, password)
        AdminBase.add_category_navigator(self)
        if parent == "":
            #  Add category
            self.driver.find_element(*CategoryPage.root_category).click()
        else:
            # Add sub category
            for category in self.driver.find_elements(*CategoryPage.parents):
                if category.text == parent:
                    category.click()
        self.driver.find_element(*CategoryPage.view_on_home).click()
        self.driver.find_element(*CategoryPage.state_online).click()
        self.driver.find_element(*CategoryPage.name).send_keys(categoryname)

        # submit
        self.driver.find_element(*CategoryPage.add_category_button).click()

        # Open edit category page
        AdminBase.edit_category_navigator(self)
        self.driver.find_element_by_link_text(categoryname).click()

        # view online
        self.driver.find_element(*CategoryPage.view_online).click()

        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        category_page_title = self.driver.find_element(*CategoryPage.page_title).text
        self.driver.close()
        self.driver.switch_to_window(window_before)
        # Check category name
        if category_page_title == categoryname:
            return True
        else:
            return False

    # delete category
    def delete_category(self, username, password,categoryname):
        # Open category page
        AdminBase.navigate_to_admin(self,username, password)
        AdminBase.edit_category_navigator(self)

        # delete category
        # get list of categories names
        for i in self.driver.find_elements_by_css_selector('tr[class="classe1"] td:nth-child(4) a'):
            if i.text == categoryname:
                ref = i.get_attribute('href')
                category_id=ref.split('=')
                id = category_id[2]
                self.driver.find_element_by_css_selector('a[href="http://10.1.22.67/Jamaica/administrer/categories.php?mode=suppr&id={}"]'.format(id)).click()
                self.driver.find_element(*CategoryPage.confirm_delete).click()
                return self.driver.find_element(*CategoryPage.alert).text
            else:
                continue




