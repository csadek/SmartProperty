from ddt import ddt, data, unpack

from POM.Administrator.CategoryPage import CategoryPage
from Utilities.BaseTestCase import BaseTestCase
from Utilities.ReadExcel import ReadExcel


@ddt
class Category(BaseTestCase):

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Categories']))
    @unpack
    def test_add_category(self,name,password,categoryname,parent):
        self.assertTrue(CategoryPage.add_category(self,name,password,categoryname,parent))

    @data(*ReadExcel.get_sheets('../Utilities/Data.xlsx',['Admin','Categories']))
    @unpack
    def test_delete_category(self,username,password,categoryname,parent):
        self.assertIn('The category {} has been deleted'.format(categoryname),CategoryPage.delete_category(self,username,password,categoryname))
