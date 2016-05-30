#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.Systest import SysPage
from ways.wms import wmsPage

class Branstore(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不勾选，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBStore()
        self.clickBatchBStoreButton()
        self.clickBatchEndBStore()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test_002(self):
        '''验证不勾选，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBStore()
        self.clickBatchBStoreButton()
        self.clickBatchStartBStore()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test_003(self):
        '''验证不选择品牌，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBStore()
        self.createBrandStore(int(self.readExcel(60, 0)), int(self.readExcel(60, 1)))
        self.assertEqual(u'店铺品牌绑定修改或新增', self.getBStitleInfo())

    def test_004(self):
        '''验证不选择店铺，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBStore()
        self.createBrandStore(int(self.readExcel(61, 0)), int(self.readExcel(61, 1)))
        self.assertEqual(u'店铺品牌绑定修改或新增', self.getBStitleInfo())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Branstore))
    unittest.TextTestRunner(verbosity=2).run(suite)