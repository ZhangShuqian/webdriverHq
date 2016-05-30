#coding:utf-8
import unittest
import time
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage

class Store(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''不勾选店铺，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickBatchStore()
        self.clickStartStore()
        self.assertEqual(u'请选择需要启用的店铺', self.getPrompt())

    def test_002(self):
        '''不勾选店铺，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickBatchStore()
        self.clickEndStore()
        self.assertEqual(u'请选择需要停用的店铺', self.getPrompt())

    def test_003(self):
        '''勾选店铺，批量停用是否有效'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickBatchStore()
        self.clickAllSelectStore()
        self.clickBatchStore()
        self.clickEndStore()
        time.sleep(1)
        self.assertEqual(u'无效', self.checkStateStore())

    def test_004(self):
        '''勾选店铺，批量启用是否有效'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickBatchStore()
        self.clickAllSelectStore()
        self.clickBatchStore()
        self.clickStartStore()
        time.sleep(1)
        self.assertEqual(u'有效', self.checkStateStore())

    def test_005(self):
        '''验证编辑店铺页面，显示店铺残次类型'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickEditButtonStore()
        self.assertEqual(u'店铺残次类型设置', self.getDefectTypeStore())

    def test_006(self):
        '''验证编辑店铺页面，显示店铺残次原因'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickEditButtonStore()
        self.assertEqual(u'店铺残次原因设置', self.getDefectReasonStore())

    def test_007(self):
        '''验证编辑店铺页面，显示物理仓列表'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickEditButtonStore()
        self.assertEqual(u'物理仓列表', self.getWarehouseStore())

    def test_008(self):
        '''验证单个停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickSingleEditStoreButton()
        self.clickSingleEndStore()
        self.assertEqual(u'无效', self.checkStateStore())

    def test_009(self):
        '''验证单个启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseStore()
        self.clickSingleEditStoreButton()
        self.clickSingleStartStore()
        self.assertEqual(u'有效', self.checkStateStore())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Store))
    unittest.TextTestRunner(verbosity=2).run(suite)
