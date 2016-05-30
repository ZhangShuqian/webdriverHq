#coding:utf-8
import unittest
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage


class Logistics(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不点击全选，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickBatchLogistic()
        self.clickEndLogistic()
        self.assertEqual(u'请选择需要停用的区域', self.getPrompt())

    def test_002(self):
        '''验证不点击全选，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickBatchLogistic()
        self.clickStartLogistic()
        self.assertEqual(u'请选择需要启用的区域', self.getPrompt())

    def test_003(self):
        '''验证物流商编码为空，是否可以保存成功'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.createLogisticButton()
        self.createLogistic(self.readExcel(1, 0), self.readExcel(1, 1))
        self.assertEqual(u'物流商维护', self.getTitleLogistic())

    def test_004(self):
        '''验证物流商名称为空，是否可以保存过成功'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.createLogisticButton()
        self.createLogistic(self.readExcel(2, 0), self.readExcel(2, 1))
        self.assertEqual(u'物流商维护', self.getTitleLogistic())

    @unittest.skip('The function was passed')
    def test_005(self):
        '''验证物流商编码/名称正确输入，保存成功'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.createLogisticButton()
        self.createLogistic(self.readExcel(3, 0), self.readExcel(3, 1))
        self.assertEqual(u'物流商列表', self.getInfoLogistic())

    def test_006(self):
        '''验证勾选物流商，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickBatchLogistic()
        self.clickAllSelectLogistic()
        self.clickBatchLogistic()
        self.clickEndLogistic()
        self.assertEqual(u'无效', self.StateInfoLogistic())

    def test_007(self):
        '''验证勾选物理商，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickBatchLogistic()
        self.clickAllSelectLogistic()
        self.clickBatchLogistic()
        self.clickStartLogistic()
        self.assertEqual(u'有效', self.StateInfoLogistic())

    def test_008(self):
        '''点击编辑按钮，是否跳转到编辑页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickEditButtonLogistics()
        self.assertEqual(u'物流商维护', self.getEditTitleLogistics())

    def test_009(self):
        '''验证单个停用Logsitics'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickSingleEditLogisticsButton()
        self.clickSingleEndLogistics()
        self.assertEqual(u'无效', self.StateInfoLogistic())

    def test_010(self):
        '''验证单个启用logistics'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseLogistic()
        self.clickSingleEditLogisticsButton()
        self.clickSingleStartLogistics()
        self.assertEqual(u'有效', self.StateInfoLogistic())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Logistics))
    unittest.TextTestRunner(verbosity=2).run(suite)