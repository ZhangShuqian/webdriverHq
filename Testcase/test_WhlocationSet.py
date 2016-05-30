#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.warehouseSet import WarePage
from ways.wms import wmsPage

class Location(Helper, DataHlper, wmsPage, WarePage):
    def test001(self):
        '''验证不勾选库位，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickBatchLocation()
        self.clickBatchEndLocation()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test002(self):
        '''验证不勾选库位，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickBatchLocation()
        self.clickBatchStartLocation()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test003(self):
        '''不勾选库位，是否可以批量删除'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickBatchLocation()
        self.clickBatchDeleteLocation()
        self.assertEqual(u'请选择需要删除的区域', self.get_prompt())

    @unittest.skip(u'有库存的库位，不允许编辑')
    def test004(self):
        '''勾选库位，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickBatchLocation()
        self.clickBatchAllSelectLocation()
        self.clickBatchLocation()
        self.clickBatchEndLocation()
        self.assertEqual(u'无效', self.getLocationStateInfo())

    @unittest.skip(u'有库存的库位，不支持编辑')
    def test005(self):
        '''勾选库位，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickBatchLocation()
        self.clickBatchAllSelectLocation()
        self.clickBatchLocation()
        self.clickBatchStartLocation()
        self.assertEqual(u'有效', self.getLocationStateInfo())

    def test006(self):
        '''验证点击库位创建按钮，是否进入创建页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickCreateLocationButton()
        self.assertEqual(u'库位创建', self.getCreateTitle())

    def test007(self):
        '''验证点击库位批量修改按钮，是否进入批量修改页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickFixLocationButton()
        self.assertEqual(u'库位批量修改', self.getFixTitle())

    def test008(self):
        '''验证点击库位批量删除按钮，是否进入批量删除页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseLocation()
        self.clickRemoveLocationButton()
        self.assertEqual(u'库位批量删除', self.getRemoveTitle())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Location))
    unittest.TextTestRunner(verbosity=2).run(suite)