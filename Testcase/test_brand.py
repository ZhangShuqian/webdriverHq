#coding:utf-8
import unittest
import time
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage


class Brand(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不勾选品牌，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickBatchBrand()
        self.clickStartBrand()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.getPrompt())

    def test_002(self):
        '''验证不勾选品牌，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickBatchBrand()
        self.clickEndBrand()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.getPrompt())

    def test_003(self):
        '''验证不勾选品牌，是否可以批量删除'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickBatchBrand()
        self.clickDeleteBrand()
        self.assertEqual(u'请至少选择一条记录进行编辑', self.getPrompt())

    def test_004(self):
        '''验证勾选品牌，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickBatchBrand()
        self.clickAllSelectBrand()
        self.clickBatchBrand()
        self.clickEndBrand()
        # time.sleep(2)
        self.assertEqual(u'无效', self.checkStateBrand())

    def test_005(self):
        '''验证勾选品牌，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickBatchBrand()
        self.clickAllSelectBrand()
        self.clickBatchBrand()
        self.clickStartBrand()
        # time.sleep(1)
        self.assertEqual(u'有效', self.checkStateBrand())

    
    def test_006(self):
        '''验证点击返回按钮，页面是否跳转到品牌列表页面'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickCreateBrandButton()
        self.clickReturnButtonBrand()
        self.assertEqual(u'品牌列表', self.getInfoBrand())
    
    def test_007(self):
        '''验证品牌编码为空，是否可以创建成功'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickCreateBrandButton()
        self.createBrand(self.readExcel(18, 0), self.readExcel(18, 1), self.readExcel(18, 2))
        self.assertEqual(u'品牌创建', self.getTitleBrand())
    
    def test_008(self):
        '''验证品牌名称为空，是否可以创建成功'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickCreateBrandButton()
        self.createBrand(self.readExcel(19, 0), self.readExcel(19, 1), self.readExcel(19, 2))
        self.assertEqual(u'品牌创建', self.getTitleBrand())
    
    def test_009(self):
        '''验证品牌英文名称为空，是否可以创建成功'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickCreateBrandButton()
        self.createBrand(self.readExcel(20, 0), self.readExcel(20, 1), self.readExcel(20, 2))
        self.assertEqual(u'品牌创建', self.getTitleBrand())

    def test_010(self):
        '''验证单个停用brand'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickSingleEditBrandButton()
        self.clickSingleEndBrand()
        self.assertEqual(u'无效', self.checkStateBrand())

    def test_011(self):
        '''验证单个启用brand'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseBrand()
        self.clickSingleEditBrandButton()
        self.clickSingleStartBrand()
        self.assertEqual(u'有效', self.checkStateBrand())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Brand))
    unittest.TextTestRunner(verbosity=2).run(suite)

