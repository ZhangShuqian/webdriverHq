#coding:utf-8
import unittest
import time
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage



class Supplier(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不勾选供应商，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickBatchSupplier()
        self.clickStartSupplier()
        self.assertEqual(u'请选择需要启用的供应商', self.getPrompt())

    def test_002(self):
        '''验证不勾选供应商，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickBatchSupplier()
        self.clickEndSupplier()
        self.assertEqual(u'请选择需要停用的供应商', self.getPrompt())

    def test_003(self):
        '''验证勾选供应商，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickBatchSupplier()
        self.clickAllSelectSupplier()
        self.clickBatchSupplier()
        self.clickEndSupplier()
        time.sleep(2)
        self.assertEqual(u'无效', self.checkStateSupplier())

    def test_004(self):
        '''验证勾选供应商，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickBatchSupplier()
        self.clickAllSelectSupplier()
        self.clickBatchSupplier()
        self.clickStartSupplier()
        time.sleep(2)
        self.assertEqual(u'有效', self.checkStateSupplier())

    def test_005(self):
        '''点击返回按钮，页面是否跳转到供应商列表页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSupplierButton()
        self.clickReturnButtonSupplier()
        self.assertEqual(u'供应商列表', self.getInfoSupplier())

    def test_006(self):
        '''点击编辑，页面是否跳转到供应商编辑页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickEditButtonSupplier()
        self.assertEqual(u'修改供应商', self.getEditTitleSupplier())

    def test_007(self):
        '''供应商编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSupplierButton()
        self.createSupplier(self.readExcel(22,0), self.readExcel(22,1), int(self.readExcel(22,2)), int(self.readExcel(22,3)),
                            int(self.readExcel(22,4)), self.readExcel(22,5), self.readExcel(22,6))
        self.assertEqual(u'创建供应商', self.getTitleSupplier())

    def test_008(self):
        '''供应商名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSupplierButton()
        self.createSupplier(self.readExcel(23, 0), self.readExcel(23, 1), int(self.readExcel(23, 2)),
                               int(self.readExcel(23, 3)), int(self.readExcel(23, 4)), self.readExcel(23, 5),
                               self.readExcel(23, 6))
        self.assertEqual(u'创建供应商', self.getTitleSupplier())

    def test_009(self):
        '''所属客户为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSupplierButton()
        self.createSupplier(self.readExcel(24, 0), self.readExcel(24, 1), int(self.readExcel(24, 2)),
                               int(self.readExcel(24, 3)), int(self.readExcel(24, 4)), self.readExcel(24, 5),
                               self.readExcel(24, 6))
        self.assertEqual(u'创建供应商', self.getTitleSupplier())

    def test_010(self):
        '''联系人为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSupplierButton()
        self.createSupplier(self.readExcel(25, 0), self.readExcel(25, 1), int(self.readExcel(25, 2)),
                               int(self.readExcel(25, 3)), int(self.readExcel(25, 4)), self.readExcel(25, 5),
                               self.readExcel(25, 6))
        self.assertEqual(u'创建供应商', self.getTitleSupplier())

    def test_011(self):
        '''联系电话为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSupplierButton()
        self.createSupplier(self.readExcel(26, 0), self.readExcel(26, 1), int(self.readExcel(26, 2)),
                               int(self.readExcel(26, 3)), int(self.readExcel(26, 4)), self.readExcel(26, 5),
                               self.readExcel(26, 6))
        self.assertEqual(u'创建供应商', self.getTitleSupplier())

    def test_012(self):
        '''验证单个停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSingleEditSupplierButton()
        self.clickSingleEndSupplier()
        self.assertEqual(u'无效', self.checkStateSupplier())

    def test_013(self):
        '''验证单个启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSupplier()
        self.clickSingleEditSupplierButton()
        self.clickSingleStartSupplier()
        self.assertEqual(u'有效', self.checkStateSupplier())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Supplier))
    unittest.TextTestRunner(verbosity=2).run(suite)