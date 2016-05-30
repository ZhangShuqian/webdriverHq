#coding:utf-8
import unittest
import time
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage


class Sku(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不勾选商品，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickBatchSku()
        self.clickStartSku()
        self.assertEqual(u'请选择需要启用的商品', self.getPrompt())

    def test_002(self):
        '''验证不勾选商品，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickBatchSku()
        self.clickEndSku()
        self.assertEqual(u'请选择需要停用的商品', self.getPrompt())

    def test_003(self):
        '''验证创建商品页面，是否默认商品基本信息为首页'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.createSkuButton()
        self.assertEqual(u'商品基本信息', self.getFirstTitle())

    def test_004(self):
        '''验证勾选商品，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickBatchSku()
        self.clickAllSelectSku()
        self.clickBatchSku()
        self.clickEndSku()
        time.sleep(3)
        self.assertEqual(u'无效', self.checkStateSku())

    def test_005(self):
        '''验证勾选商品，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickBatchSku()
        self.clickAllSelectSku()
        self.clickBatchSku()
        self.clickStartSku()
        time.sleep(3)
        self.assertEqual(u'有效', self.checkStateSku())

    def test_006(self):
        '''验证点击返回按钮，页面是否跳转到商品列表页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickCreateSkuButton()
        self.clickReturnButtonSku()
        self.assertEqual(u'商品列表', self.getInfoSku())

    def test_007(self):
        '''验证单个停用SKU'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickSingleEditSKuButton()
        self.clickSingleEndSKu()
        self.assertEqual(u'无效', self.checkStateSku())

    def test_008(self):
        '''验证单个启用SKU'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSku()
        self.clickSingleEditSKuButton()
        self.clickSingleStartSku()
        self.assertEqual(u'有效', self.checkStateSku())

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Sku))
    unittest.TextTestRunner(verbosity=2).run(suite)