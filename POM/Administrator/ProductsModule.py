import os
from selenium.webdriver.common.by import By
from POM.Administrator.AdminBase import AdminBase
from selenium.common.exceptions import NoSuchElementException


class ProductsModule(AdminBase):
    """ this class represents product page elements manipulations and functions. Administrator should be able to:
     - Add new products for specific categories
     - Edit existing product
     - Delete product at specific category or subcategory"""
    # Locators
    # first tab
    category = (By.CSS_SELECTOR,'#categories > option')
    position = (By.NAME,'position')
    our_selection = (By.NAME, 'on_special')
    new = (By.NAME,'on_new' )
    special = (By.NAME,'on_promo')
    reseller = (By.NAME,'on_reseller')
    best_seller = (By.NAME,'on_top')
    recommended = (By.NAME,'recommanded_product_on_cart_page')
    best= (By.NAME,'on_rollover')
    state_online = (By.NAME, 'etat')
    reference = (By.NAME,'reference')
    code = (By.NAME,'technical_code')
    price = (By.NAME,'prix')
    colors = (By.CSS_SELECTOR,'select[name="couleurs[]"] option')

    # Second tab
    english_tab = (By.CSS_SELECTOR,'a[href="#tab_EN"]')
    product_name = (By.CSS_SELECTOR,'#tab_EN > input:nth-child(3)')
    short_description = (By.NAME,'descriptif_en')
    description = (By.CSS_SELECTOR,'body')
    content_tab1 = (By.NAME,'tab1_title_en')
    content_tab2 = (By.NAME,'tab2_title_en')
    save_content = (By.CSS_SELECTOR,'#total > div.container > div > div > form > table > tbody > tr:nth-child(21) > td > input')
    confirm_tab2 =(By.CLASS_NAME,'alert alert-success fade in')

    # Third tab
    file_associated_tab = (By.CSS_SELECTOR,'a[href="#tab2"]')
    add_image = (By.CSS_SELECTOR,'tr>td[class="title_label"]>a')
    chose_file_button = (By.XPATH,'//*[@id="td_0"]/table/tbody/tr[1]/td/input')
    image_upload_button = (By.CSS_SELECTOR,'input[type="file"]')

    # Save & notify
    save_button = (By.CSS_SELECTOR,'#total > div.container > div > div > form > div.center > p > input')
    confirm_delete = (By.CSS_SELECTOR,'body > div.bootbox.modal.fade.in > div > div > div.modal-footer > button.btn.btn-primary')
    confirm_msg =(By.CSS_SELECTOR,'#total > div.container > div > div > div.alert.alert-success.fade.in > b')
    page_title = (By.CSS_SELECTOR,'#page_title > h1')

    # Add Product
    def AddProduct(self,username,password,position,reference,code,price,name,short,description):
        # Open Add product page
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.add_product_navigator(self)
        # Add first
        self.driver.find_element(*ProductsModule.category).click()
        self.driver.find_element(*ProductsModule.position).clear()
        self.driver.find_element(*ProductsModule.position).send_keys(position)
        self.driver.find_element(*ProductsModule.our_selection).click()
        self.driver.find_element(*ProductsModule.new).click()
        self.driver.find_element(*ProductsModule.special).click()
        self.driver.find_element(*ProductsModule.reseller).click()
        self.driver.find_element(*ProductsModule.recommended).click()
        self.driver.find_element(*ProductsModule.best).click()
        self.driver.find_element(*ProductsModule.state_online).click()
        self.driver.find_element(*ProductsModule.reference).send_keys(reference)
        self.driver.find_element(*ProductsModule.code).send_keys(code)
        self.driver.find_element(*ProductsModule.price).send_keys(price)
        self.driver.find_elements(*ProductsModule.colors)[1].click()
        # add second tab
        self.driver.find_element(*ProductsModule.english_tab).click()
        self.driver.find_element(*ProductsModule.product_name).send_keys(name)
        self.driver.find_element(*ProductsModule.short_description).send_keys(short)
        self.driver.find_element(*ProductsModule.description).send_keys(description)
        # submit
        self.driver.find_element(*ProductsModule.save_button).click()
        return self.driver.find_element(*ProductsModule.confirm_msg).text

    #upload image to product
    def uppload_image(self,username,password,name):
        # Add product details
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.edit_product_navigator(self)
        self.driver.find_element_by_css_selector('a[title="Delete {}"]+a[title="Modify"]'.format(name)).click()
        #edit Third tab - Jihad
        self.driver.find_element(*ProductsModule.file_associated_tab).click()
        try:
            self.driver.find_element(*ProductsModule.add_image).click()
        except NoSuchElementException :
            return "Product already has image uploaded or no colors selected for that product"

        self.driver.find_element(*ProductsModule.chose_file_button).send_keys('C:\\Users\\csadek\\Desktop\\Jamaica4.jpg')
        self.driver.find_element(*ProductsModule.save_button).click()

    # edit product details
    def edit_product(self,username,password,name,tab1,tab2):
        # Add product details
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.edit_product_navigator(self)

        modify_product = self.driver.find_element_by_css_selector('a[title="Delete {}"]+a[title="Modify"]'.format(name)).get_attribute('href')
        product_id=modify_product.split('&')
        idmsg = product_id[1].split('=')
        id = idmsg[1]
        self.driver.find_element_by_css_selector('a[title="Delete {}"]+a[title="Modify"]'.format(name)).click()
        self.driver.find_element(*ProductsModule.english_tab).click()
        self.driver.find_element_by_css_selector('a[href="http://10.1.22.67/Jamaica/administrer/produits.php?mode=modif_tab&id={}&tab_lang=en"]'.format(id)).click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.find_element(*ProductsModule.content_tab1).clear()
        self.driver.find_element(*ProductsModule.content_tab1).send_keys(tab1)
        self.driver.find_element(*ProductsModule.content_tab2).clear()
        self.driver.find_element(*ProductsModule.content_tab2).send_keys(tab2)
        self.driver.find_element(*ProductsModule.save_content).click()
        alert= self.driver.find_element(*ProductsModule.confirm_tab2).text
        self.driver.close()
        self.driver.switch_to_window(window_before)
        return alert

    # delete product
    def delete_product(self,username,password,name):
        AdminBase.navigate_to_admin(self,username,password)
        AdminBase.edit_product_navigator(self)
        self.driver.find_element_by_css_selector('a[title="Delete {}"]'.format(name)).click()
        self.driver.find_element(*ProductsModule.confirm_delete).click()



