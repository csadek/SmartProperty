import datetime
import re  # for date time format
from dateutil import parser
from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase


class FlashSalePage(AdminBase):
    """ this class represents add flash sale to specific product elements manipulations and functions"""
    """ Flash sale is specific type of sale on the product which remains for specific time- AT Jamaica"""

    # Flash Sale locators
    page_title = (By.CSS_SELECTOR,'#page_title > h1')
    flash_sale_price = (By.NAME,'prix_flash')
    start_date = (By.NAME, 'flash_start')
    end_date = (By.NAME, 'flash_end')
    show_in_flash_section =(By.NAME, 'on_flash')
    save_changes_button = (By.CSS_SELECTOR,'input[class="btn btn-primary"')
    alert = (By.CSS_SELECTOR,'div[class="alert alert-success fade in"]')

    # product locators
    view_online = (By.CSS_SELECTOR,'#page_title > h1 > a')
    price = (By.ID,'prix_80')
    old_price = (By.CSS_SELECTOR,'td[class="middle"] del')
    remaining_time = (By.CSS_SELECTOR,'div.alert.alert-warning')

    # Add flash sale
    def add_flash_sale_to_product(self,username,password,price,start,end,name):
        # Open edit product page
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.edit_product_navigator(self)
        self.driver.find_element_by_css_selector('a[title="Delete {}"]+a[title="Modify"]'.format(name)).click()

        # add flash sale
        self.driver.find_element(*FlashSalePage.flash_sale_price).clear()
        self.driver.find_element(*FlashSalePage.flash_sale_price).send_keys(int(price))
        self.driver.find_element(*FlashSalePage.start_date).click()
        self.driver.find_element(*FlashSalePage.start_date).clear()
        self.driver.find_element(*FlashSalePage.start_date).send_keys(start)
        self.driver.find_element(*FlashSalePage.end_date).click()
        self.driver.find_element(*FlashSalePage.end_date).clear()
        self.driver.find_element(*FlashSalePage.end_date).send_keys(end)

        # submit
        self.driver.find_element(*FlashSalePage.save_changes_button).click()
        return self.driver.find_element(*FlashSalePage.alert).text

    def verify_flash_sale_price(self,username,password,productname):
        # user can call that function from different views (product, admin, landing page)
        # Open edit product page
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.edit_product_navigator(self)
        self.driver.find_element_by_css_selector('a[title="Delete {}"]+a[title="Modify"]'.format(productname)).click()

        # view online
        self.driver.find_element(*FlashSalePage.view_online).click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        new = self.driver.find_element(*FlashSalePage.price).text
        self.driver.close()
        self.driver.switch_to_window(window_before)

        # extract product new price
        whole_text = new.split(',')
        exact_price = whole_text[0]
        return int(exact_price)

    def verify_remaining_time_to_end_sale(self,username,password,productname,end_time):
       # user can call that function from different views (product, admin, landing page)
        # Open edit product page
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.edit_product_navigator(self)
        self.driver.find_element_by_css_selector('a[title="Delete {}"]+a[title="Modify"]'.format(productname)).click()

        # view online
        self.driver.find_element(*FlashSalePage.view_online).click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        alert1 = self.driver.find_element(*FlashSalePage.remaining_time).text
        self.driver.close()
        self.driver.switch_to_window(window_before)

        time_list = re.findall(r'(?:\d)?\d+', alert1)
        now = datetime.datetime.now()
        remaining_time = parser.parse(end_time) - now
        if remaining_time.days == time_list[0]:
            return True
        else:
            return False
