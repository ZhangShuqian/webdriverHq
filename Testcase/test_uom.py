#coding:utf-8
import unittest
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage


class Uom(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不点击全选，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickBatchUom()
        self.clickEndUom()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.getPrompt())

    def test_002(self):
        '''验证不点击全选，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickBatchUom()
        self.clickStartUom()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.getPrompt())

    def test_003(self):
        '''验证单位类型为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickUomButton()
        self.createUom(int(self.readExcel(5, 0)), self.readExcel(5, 1), self.readExcel(5, 2), self.readExcel(5, 3))
        self.assertEqual(u'创建度量单位', self.getTitleUom())

    def test_004(self):
        '''验证单位名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickUomButton()
        self.createUom(int(self.readExcel(6, 0)), self.readExcel(6, 1), self.readExcel(6, 2), self.readExcel(6, 3))
        self.assertEqual(u'创建度量单位', self.getTitleUom())

    def test_005(self):
        '''验证单位符号为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickUomButton()
        self.createUom(int(self.readExcel(7, 0)), self.readExcel(7, 1), self.readExcel(7, 2), self.readExcel(7, 3))
        self.assertEqual(u'创建度量单位', self.getTitleUom())

    def test_006(self):
        '''验证换算率为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickUomButton()
        self.createUom(int(self.readExcel(8, 0)), self.readExcel(8, 1), self.readExcel(8, 2), self.readExcel(8, 3))
        self.assertEqual(u'创建度量单位', self.getTitleUom())

    def test_007(self):
        '''验证勾选度量单位，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickBatchUom()
        self.clickAllSelectUom()
        self.clickBatchUom()
        self.clickEndUom()
        self.assertEqual(u'无效', self.getStateUom())

    def test_008(self):
        '''验证勾选度量单位，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickBatchUom()
        self.clickAllSelectUom()
        self.clickBatchUom()
        self.clickStartUom()
        self.assertEqual(u'有效', self.getStateUom())

    def test_009(self):
        '''验证是否可以单个停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickSingleEditUomButton()
        self.clickSingleEndUom()
        self.assertEqual(u'无效', self.getStateUom())

    def test_010(self):
        '''验证是否可以单个启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseUom()
        self.clickSingleEditUomButton()
        self.clickSingleStartUom()
        self.assertEqual(u'有效', self.getStateUom())

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Uom))
    unittest.TextTestRunner(verbosity=2).run(suite)