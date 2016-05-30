#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.wms import wmsPage
from ways.Systest import SysPage

class Sysdictionary(Helper, DataHlper, wmsPage, SysPage):
    def test001(self):
        '''验证不勾选系统参数，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSysdictionary()
        self.clickBatchSysdictionary()
        self.clickBatchEndSysdic()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.get_prompt())

    def test002(self):
        '''验证不勾选系统参数，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSysdictionary()
        self.clickBatchSysdictionary()
        self.clickBatchStartSysdic()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.get_prompt())

    def test003(self):
        '''验证不选择组别名称(组别编码)，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSysdictionary()
        self.clickCreateSysdicButton()
        self.createSysdictonary(int(self.readExcel(49, 0)), self.readExcel(49, 1), self.readExcel(49, 2))
        self.assertEqual(u'系统配置参数添加', self.getSysdicTitle())

    def test004(self):
        '''验证参数名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSysdictionary()
        self.clickCreateSysdicButton()
        self.createSysdictonary(int(self.readExcel(50, 0)), self.readExcel(50, 1), self.readExcel(50, 2))
        self.assertEqual(u'系统配置参数添加', self.getSysdicTitle())

    def test005(self):
        '''验证参数编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseSysdictionary()
        self.clickCreateSysdicButton()
        self.createSysdictonary(int(self.readExcel(51, 0)), self.readExcel(51, 1), self.readExcel(51, 2))
        self.assertEqual(u'系统配置参数添加', self.getSysdicTitle())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Sysdictionary))
    unittest.TextTestRunner(verbosity=2).run(suite)