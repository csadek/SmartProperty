from selenium.webdriver.common.by import By
from POM.Customer.CustomerBase import CustomerBase
from selenium.common.exceptions import NoSuchElementException


class SearchPage(CustomerBase):

    SearchBox = (By.NAME,'search')
    CategoryList = (By.ID,'search_category')
    SearchButton =  (By.CLASS_NAME,'btn-header_search')
    list_of_products = (By.CSS_SELECTOR, 'div[class="produits row allow_order"] > div')

    def search_data(self,ProductName,CategoryName):
        if ProductName != '' or CategoryName != '':
            self.driver.find_element(*SearchPage.SearchBox).send_keys(ProductName)
            self.driver.find_element(*SearchPage.CategoryList).send_keys(CategoryName)
            self.driver.find_element(*SearchPage.SearchButton).click()
            products_search= "No products found"
            try:
                self.driver.find_elements(*SearchPage.list_of_products)
            except NoSuchElementException:
                return products_search
            no_of_products = len(self.driver.find_elements(*SearchPage.list_of_products))
            if no_of_products == 0 :
                return  products_search
            products_search = "we found {} products which matches your search criteria".format(no_of_products)
            return products_search
        else:
            return "No data entered"
