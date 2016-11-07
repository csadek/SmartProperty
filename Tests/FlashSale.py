from ddt import ddt, data, unpack

from POM.Administrator.FlashSalePage import FlashSalePage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class FlashSale(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','flash']))
    @unpack
    def test_Add_flash_sale(self,username,password,amount,start,end,product_name):
        self.assertIn('×\nChanges to product {} have been taken into account.'.format(product_name),FlashSalePage.add_flash_sale_to_product(self,username,password,amount,start,end,product_name))
        self.assertEqual(amount,FlashSalePage.verify_flash_sale_price(self,username,password, product_name))
        self.assertTrue(True, FlashSalePage.verify_remaining_time_to_end_sale(self,username,password,product_name,end))
