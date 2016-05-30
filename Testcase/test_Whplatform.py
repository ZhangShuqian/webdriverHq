#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.warehouseSet import WarePage
from ways.wms import wmsPage

class Platform(Helper, DataHlper, wmsPage, WarePage):
    def test_001(self):
        '''验证不勾选月台，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.clickBatchPlatform()
        self.clickBatchEndPlatform()
        self.assertEqual(u'请选择需要停用的月台', self.get_prompt())

    def test_002(self):
        '''验证不勾选月台，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.clickBatchPlatform()
        self.clickBatchStartPlatform()
        self.assertEqual(u'请选择需要启用的月台', self.get_prompt())

    def test_003(self):
        '''验证勾选月台，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.clickBatchPlatform()
        self.clickBatchAllSelePlatform()
        self.clickBatchPlatform()
        self.clickBatchEndPlatform()
        self.assertEqual(u'停用', self.getStatePlatform())

    def test_004(self):
        '''验证勾选月台，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.clickBatchPlatform()
        self.clickBatchAllSelePlatform()
        self.clickBatchPlatform()
        self.clickBatchStartPlatform()
        self.assertEqual(u'启用', self.getStatePlatform())

    def test_005(self):
        '''验证是否可以单个停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.clickSingleEditPlatformButton()
        self.clickSingleEndPlatform()
        self.assertEqual(u'停用', self.getStatePlatform())

    def test_006(self):
        '''验证是否可以单个启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.clickSingleEditPlatformButton()
        self.clickSingleStartPlatform()
        self.assertEqual(u'启用', self.getStatePlatform())

    def test_007(self):
        '''验证月台编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.createPlatform(self.readExcel(69, 0), self.readExcel(69, 1), int(self.readExcel(69, 2)))
        self.assertEqual(u'创建月台', self.getplatformTitle())

    def test_008(self):
        '''验证月台名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.createPlatform(self.readExcel(70, 0), self.readExcel(70, 1), int(self.readExcel(70, 2)))
        self.assertEqual(u'创建月台', self.getplatformTitle())

    def test_009(self):
        '''验证月台类型不选择，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBasePlatform()
        self.createPlatform(self.readExcel(71, 0), self.readExcel(71, 1), int(self.readExcel(71, 2)))
        self.assertEqual(u'创建月台', self.getplatformTitle())

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Platform))
    unittest.TextTestRunner(verbosity=2).run(suite)