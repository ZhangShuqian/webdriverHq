#coding:utf-8
import unittest
from selenium import webdriver
from ways.wms import wmsPage
from ways.warehouseSet import WarePage
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper

class Area(Helper, DataHlper, wmsPage, WarePage):
    def test001(self):
        '''验证不勾选物流商，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickBatchAreaButton()
        self.clickStartArea()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test002(self):
        '''验证不勾选物流商，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickBatchAreaButton()
        self.clickEndArea()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test003(self):
        '''验证区域编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickCreateAreaButton()
        self.createArea(self.readExcel(28, 0), self.readExcel(28, 1), int(self.readExcel(28, 2)))
        self.assertNotEqual(u'区域列表', self.getInfoTitle())

    def test004(self):
        '''验证区域名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickCreateAreaButton()
        self.createArea(self.readExcel(29, 0), self.readExcel(29, 1), int(self.readExcel(29, 2)))
        self.assertNotEqual(u'区域列表', self.getInfoTitle())

    def test005(self):
        '''验证勾选物流商，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickBatchAreaButton()
        self.clickAllSelectArea()
        self.clickBatchAreaButton()
        self.clickEndArea()
        self.assertEqual(u'无效', self.getStateInfoArea())

    def test006(self):
        '''验证勾选物流商，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickBatchAreaButton()
        self.clickAllSelectArea()
        self.clickBatchAreaButton()
        self.clickStartArea()
        self.assertEqual(u'有效', self.getStateInfoArea())

    def test007(self):
        '''验证是否可以单个停用物流商'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickSingleEditButton()
        self.clickSingleEndArea()
        self.assertEqual(u'无效', self.getStateInfoArea())

    def test008(self):
        '''验证是否可以单个启用物流商'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseArea()
        self.clickSingleEditButton()
        self.clickSingleStartArea()
        self.assertEqual(u'有效', self.getStateInfoArea())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Area))
    unittest.TextTestRunner(verbosity=2).run(suite)