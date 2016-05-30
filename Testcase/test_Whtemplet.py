#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.warehouseSet import WarePage
from ways.wms import wmsPage

class Templet(Helper, DataHlper, WarePage, wmsPage):
    def test_001(self):
        '''验证不勾选库位模板，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickBatchTempletButton()
        self.clickBatchEndTemplet()
        self.assertEqual(u'请选择需要停用的库位模版', self.get_prompt())

    def test_002(self):
        '''验证不勾选库位模板，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickBatchTempletButton()
        self.clickBatchStartTemplet()
        self.assertEqual(u'请选择需要启用的库位模版', self.get_prompt())

    def test_003(self):
        '''验证勾选库位模板，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickBatchTempletButton()
        self.clickBatchAllSelectTemplet()
        self.clickBatchTempletButton()
        self.clickBatchEndTemplet()
        self.assertEqual(u'无效', self.getTempletStateInfo())

    def test_004(self):
        '''验证勾选库位模板，是否可批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickBatchTempletButton()
        self.clickBatchAllSelectTemplet()
        self.clickBatchTempletButton()
        self.clickBatchStartTemplet()
        self.assertEqual(u'有效', self.getTempletStateInfo())

    def test_005(self):
        '''验证是否可以单个停用库位模板'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickSingleEditTempletButton()
        self.clickSingleEndTemplet()
        self.assertEqual(u'无效', self.getTempletStateInfo())

    def test_006(self):
        '''验证是否可以单个启用库位模板'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickSingleEditTempletButton()
        self.clickSingleStartTemplet()
        self.assertEqual(u'有效', self.getTempletStateInfo())

    def test_007(self):
        '''验证不创建维度，是否可以保存库位模板'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(38, 0), self.readExcel(38, 1), self.readExcel(38, 2), self.readExcel(38, 3),
                           self.readExcel(38, 4), self.readExcel(38, 5), self.readExcel(38, 6))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_008(self):
        '''验证库位模板名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(39, 0), self.readExcel(39, 1), self.readExcel(39, 2), self.readExcel(39, 3),
                           self.readExcel(39, 4), self.readExcel(39, 5), self.readExcel(39, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_009(self):
        '''验证库位模板编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(40, 0), self.readExcel(40, 1), self.readExcel(40, 2), self.readExcel(40, 3),
                           self.readExcel(40, 4), self.readExcel(40, 5), self.readExcel(40, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_010(self):
        '''验证库位长为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(41, 0), self.readExcel(41, 1), self.readExcel(41, 2), self.readExcel(41, 3),
                           self.readExcel(41, 4), self.readExcel(41, 5), self.readExcel(41, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_011(self):
        '''验证库位模板宽为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(42, 0), self.readExcel(42, 1), self.readExcel(42, 2), self.readExcel(42, 3),
                           self.readExcel(42, 4), self.readExcel(42, 5), self.readExcel(42, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_012(self):
        '''验证库位高为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(43, 0), self.readExcel(43, 1), self.readExcel(43, 2), self.readExcel(43, 3),
                           self.readExcel(43, 4), self.readExcel(43, 5), self.readExcel(43, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_013(self):
        '''验证库位体积为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(44, 0), self.readExcel(44, 1), self.readExcel(44, 2), self.readExcel(44, 3),
                           self.readExcel(44, 4), self.readExcel(44, 5), self.readExcel(44, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_014(self):
        '''验证库位重量为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.createTemplet(self.readExcel(45, 0), self.readExcel(45, 1), self.readExcel(45, 2), self.readExcel(45, 3),
                           self.readExcel(45, 4), self.readExcel(45, 5), self.readExcel(45, 6))
        self.clickAddDimensionalityButton()
        self.createDimensionality(self.readExcel(47, 0))
        self.clickSaveTempletButton()
        self.assertEqual(u'库位模板配置', self.getCreateTempletInfo())

    def test_015(self):
        '''验证库位模板是否可以增加维度'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseTemplet()
        self.clickCreateTempletButton()
        self.clickAddDimensionalityButton()
        self.clickPlusDimensionality()
        self.assertEqual(u'维度2', self.getDimensionalityName())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Templet))
    unittest.TextTestRunner(verbosity=2).run(suite)