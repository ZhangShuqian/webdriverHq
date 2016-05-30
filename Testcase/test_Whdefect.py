#coding:utf-8
from selenium import webdriver
import unittest
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.warehouseSet import WarePage
from ways.wms import wmsPage

class Defect(Helper, DataHlper, wmsPage, WarePage):
    def test001(self):
        '''验证点击编辑按钮，页面是否跳转到编辑页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickEditDefectButton()
        self.assertEqual(u'编辑仓库残次信息', self.getEditTitleInfo())

    def test002(self):
        '''验证是否可以单个停用仓库残次类型'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickSingleEditDefectButton()
        self.clickSingleEndDefectButton()
        self.assertEqual(u'停用', self.getStateInfoDefect())


    def test003(self):
        '''验证是否可以单个启用仓库残次类型'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickSingleEditDefectButton()
        self.clickSingleStartDefectButton()
        self.assertEqual(u'启用', self.getStateInfoDefect())

    def test004(self):
        '''验证残次类型编码不能为空'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickCreateDefectButton()
        self.createDefectType(self.readExcel(31, 0), self.readExcel(31, 1))
        self.clickSaveDefectButton()
        self.assertEqual(u'必填字段不能为空', self.get_prompt())

    def test005(self):
        '''验证残次类型名称不能为空'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickCreateDefectButton()
        self.createDefectType(self.readExcel(32, 0), self.readExcel(32, 1))
        self.clickSaveDefectButton()
        self.assertEqual(u'必填字段不能为空', self.get_prompt())

    def test006(self):
        '''验证不添加残次类型，不可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickCreateDefectButton()
        self.createDefectType(self.readExcel(33, 0), self.readExcel(33, 1))
        self.clickSaveDefectButton()
        self.assertEqual(u'请添加仓库残次原因', self.get_prompt())

    # @unittest.skip('The Model has the bug')
    def test007(self):
        '''验证残次原因编码，不能为空'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickCreateDefectButton()
        self.createDefectType(self.readExcel(33, 0), self.readExcel(33, 1))
        self.clickAddDefectReasonButton()
        self.defectReasonName(self.readExcel(35, 1))
        self.defectReasonCode(self.readExcel(35, 0))
        self.clickSaveDefectButton()
        self.assertEqual(u'请填写仓库残次原因编码', self.get_prompt())

    # @unittest.skip('The Model has the bug')
    def test008(self):
        '''验证残次原因名称，不能为空'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        #self.clickBaseWarehouse()
        self.clickBaseDefect()
        self.clickCreateDefectButton()
        self.createDefectType(self.readExcel(33, 0), self.readExcel(33, 1))
        self.clickAddDefectReasonButton()
        self.defectReasonCode(self.readExcel(36, 0))
        self.defectReasonName(self.readExcel(36, 1))
        self.clickSaveDefectButton()
        self.assertEqual(u'请填写仓库残次原因名称', self.get_prompt())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Defect))
    unittest.TextTestRunner(verbosity=2).run(suite)