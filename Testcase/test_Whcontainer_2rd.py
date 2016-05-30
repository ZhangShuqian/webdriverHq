#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.warehouseSet import WarePage
from ways.wms import wmsPage

class Container(Helper, DataHlper, wmsPage, WarePage):
    def test001(self):
        '''验证不勾选二级容器，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.clickBatchContainerButton()
        self.clickBatchEndContainer()
        self.assertEqual(u'请选择需要停用的容器', self.get_prompt())

    def test002(self):
        '''验证不勾选二级容器，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.clickBatchContainerButton()
        self.clickBatchStartContainer()
        self.assertEqual(u'请选择需要启用的容器', self.get_prompt())

    def test003(self):
        '''验证勾选二级容器，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.clickBatchContainerButton()
        self.clickBatchAllSelectContainer()
        self.clickBatchContainerButton()
        self.clickBatchEndContainer()
        self.assertEqual(u'无效', self.getContainerState())

    def test004(self):
        '''验证勾选二级容器，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.clickBatchContainerButton()
        self.clickBatchAllSelectContainer()
        self.clickBatchContainerButton()
        self.clickBatchStartContainer()
        self.assertEqual(u'有效', self.getContainerState())

    def test005(self):
        '''验证是否可以单个停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.clickSingleEditContainer()
        self.clickSingleEndContainer()
        self.assertEqual(u'无效', self.getContainerState())

    def test006(self):
        '''验证是否可以单个启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.clickSingleEditContainer()
        self.clickSingleStartContainer()
        self.assertEqual(u'有效', self.getContainerState())

    def test007(self):
        '''验证二级容器名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.createContainer(int(self.readExcel(63, 0)), self.readExcel(63, 1), self.readExcel(63, 2), int(self.readExcel(63, 3)),
                             self.readExcel(63, 4), self.readExcel(63, 5), self.readExcel(63, 6), int(self.readExcel(63, 7)),
                             self.readExcel(63, 8), int(self.readExcel(63, 9)), self.readExcel(63, 10), int(self.readExcel(63, 11)))
        self.assertEqual(u'创建二级容器', self.getInfoTitleContainer())

    def test008(self):
        '''验证二级容器编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.createContainer(int(self.readExcel(64, 0)), self.readExcel(64, 1), self.readExcel(64, 2), int(self.readExcel(64, 3)),
                             self.readExcel(64, 4), self.readExcel(64, 5), self.readExcel(64, 6), int(self.readExcel(64, 7)),
                             self.readExcel(64, 8), int(self.readExcel(64, 9)), self.readExcel(64, 10), int(self.readExcel(64, 11)))
        self.assertEqual(u'创建二级容器', self.getInfoTitleContainer())

    def test009(self):
        '''验证长宽高为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.createContainer(int(self.readExcel(65, 0)), self.readExcel(65, 1), self.readExcel(65, 2), int(self.readExcel(65, 3)),
                             self.readExcel(65, 4), self.readExcel(65, 5), self.readExcel(65, 6), int(self.readExcel(65, 7)),
                             self.readExcel(65, 8), int(self.readExcel(65, 9)), self.readExcel(65, 10), int(self.readExcel(65, 11)))
        self.assertEqual(u'创建二级容器', self.getInfoTitleContainer())

    def test010(self):
        '''验证体积为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.createContainer(int(self.readExcel(66, 0)), self.readExcel(66, 1), self.readExcel(66, 2), int(self.readExcel(66, 3)),
                             self.readExcel(66, 4), self.readExcel(66, 5), self.readExcel(66, 6), int(self.readExcel(66, 7)),
                             self.readExcel(66, 8), int(self.readExcel(66, 9)), self.readExcel(66, 10), int(self.readExcel(66, 11)))
        self.assertEqual(u'创建二级容器', self.getInfoTitleContainer())

    def test011(self):
        '''验证重量为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        # self.clickBaseWarehouse()
        self.clickBaseContainer()
        self.createContainer(int(self.readExcel(67, 0)), self.readExcel(67, 1), self.readExcel(67, 2), int(self.readExcel(67, 3)),
                             self.readExcel(67, 4), self.readExcel(67, 5), self.readExcel(67, 6), int(self.readExcel(67, 7)),
                             self.readExcel(67, 8), int(self.readExcel(67, 9)), self.readExcel(67, 10), int(self.readExcel(67, 11)))
        self.assertEqual(u'创建二级容器', self.getInfoTitleContainer())

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Container))
    unittest.TextTestRunner(verbosity=2).run(suite)