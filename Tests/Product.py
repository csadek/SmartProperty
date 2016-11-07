from ddt import ddt, data, unpack
from POM.Administrator.ProductsModule import ProductsModule
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class Product(BaseTestCase):

    """@data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Clothes']))
    @unpack
    def test_Add_Product(self,username,password,position,reference,code,price,name,short,description):
        self.assertIn(name,ProductsModule.AddProduct(self,username,password,int(position),reference,code,int(price),name,short,description))

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Clothes']))
    @unpack
    def test_pdelete(self,username,password,position,reference,code,price,name,short,description):
        ProductsModule.delete_product(self,username,password,name)"""

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Product instructions']))
    @unpack
    def test_edit_product(self,username,password,name,tab1,tab2):
        ProductsModule.uppload_image(self,username,password,name)
        ProductsModule.edit_product(self,username,password,name,tab1,tab2)

