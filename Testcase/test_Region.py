#coding:utf-8
from selenium import webdriver
import unittest
from Model.baseNumber import DataHlper
from Model.BaseSet import Helper
from ways.Systest import SysPage
from ways.wms import wmsPage

class Region(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证主页面默认界面是否为国家列表'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.assertEqual(u'国家列表', self.getListTitle())

    def test_002(self):
        '''验证是否可以切换到省列表主页'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickProvinceList()
        self.assertEqual(u'省列表', self.getListTitle())

    def test_003(self):
        '''验证是否可以切换到市列表主页'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickCityList()
        self.assertEqual(u'市列表', self.getListTitle())

    def test_004(self):
        '''验证是否可以切换到区列表主页'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickAreaList()
        self.assertEqual(u'区列表', self.getListTitle())

    def test_005(self):
        '''验证不勾选国家，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickBatchRegionButton()
        self.clickBatchEndRegion()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test_006(self):
        '''验证不勾选国家，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickBatchRegionButton()
        self.clickBatchStartRegion()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test_007(self):
        '''验证不勾选国家，是否可以批量删除'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickBatchRegionButton()
        self.clickBatchDeleteRegion()
        self.assertEqual(u'请选择需要删除的区域', self.get_prompt())

    def test_008(self):
        '''验证不勾选省，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickProvinceList()
        self.clickBatchRegionButton()
        self.clickBatchEndRegion()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test_009(self):
        '''验证不勾选省，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickProvinceList()
        self.clickBatchRegionButton()
        self.clickBatchStartRegion()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test_010(self):
        '''验证不勾选省，是否可以批量删除'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickProvinceList()
        self.clickBatchRegionButton()
        self.clickBatchDeleteRegion()
        self.assertEqual(u'请选择需要删除的区域', self.get_prompt())

    def test_011(self):
        '''验证不勾选市，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickCityList()
        self.clickBatchRegionButton()
        self.clickBatchEndRegion()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test_012(self):
        '''验证不勾选市，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickCityList()
        self.clickBatchRegionButton()
        self.clickBatchStartRegion()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test_013(self):
        '''验证不勾选市，是否可以批量删除'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickCityList()
        self.clickBatchRegionButton()
        self.clickBatchDeleteRegion()
        self.assertEqual(u'请选择需要删除的区域', self.get_prompt())

    def test_014(self):
        '''验证不勾选区，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickAreaList()
        self.clickBatchRegionButton()
        self.clickBatchEndRegion()
        self.assertEqual(u'请选择需要停用的区域', self.get_prompt())

    def test_015(self):
        '''验证不勾选区，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickAreaList()
        self.clickBatchRegionButton()
        self.clickBatchStartRegion()
        self.assertEqual(u'请选择需要启用的区域', self.get_prompt())

    def test_016(self):
        '''验证不勾选区，是否可以批量删除'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.clickAreaList()
        self.clickBatchRegionButton()
        self.clickBatchDeleteRegion()
        self.assertEqual(u'请选择需要删除的区域', self.get_prompt())

    def test_017(self):
        '''验证国家名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createCountry(self.readExcel(53, 0), self.readExcel(53, 1))
        self.assertEqual(u'国家信息维护', self.getTitleInfo())

    def test_018(self):
        '''验证国家编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createCountry(self.readExcel(54, 0), self.readExcel(54, 1))
        self.assertEqual(u'国家信息维护', self.getTitleInfo())

    def test_019(self):
        '''验证不选择国家，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createProvince(int(self.readExcel(56, 0)), self.readExcel(56, 1), self.readExcel(56, 2))
        self.assertEqual(u'省信息维护', self.getTitleInfo())

    def test_020(self):
        '''验证省名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createProvince(int(self.readExcel(57, 0)), self.readExcel(57, 1), self.readExcel(57, 2))
        self.assertEqual(u'省信息维护', self.getTitleInfo())

    def test_021(self):
        '''验证省编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createProvince(int(self.readExcel(58, 0)), self.readExcel(58, 1), self.readExcel(58, 2))
        self.assertEqual(u'省信息维护', self.getTitleInfo())

    def test_022(self):
        '''验证不选择国家、省，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createCity(int(self.readExcel(56, 0)), self.readExcel(56, 1), self.readExcel(56, 2))
        self.assertEqual(u'市信息维护', self.getTitleInfo())

    def test_023(self):
        '''验证市名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createCity(int(self.readExcel(57, 0)), self.readExcel(57, 1), self.readExcel(57, 2))
        self.assertEqual(u'市信息维护', self.getTitleInfo())

    def test_024(self):
        '''验证市编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createCity(int(self.readExcel(58, 0)), self.readExcel(58, 1), self.readExcel(58, 2))
        self.assertEqual(u'市信息维护', self.getTitleInfo())

    def test_025(self):
        '''验证不选择国家、省、市，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createArea(int(self.readExcel(56, 0)), self.readExcel(56, 1), self.readExcel(56, 2))
        self.assertEqual(u'区信息维护', self.getTitleInfo())

    def test_026(self):
        '''验证省名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createArea(int(self.readExcel(57, 0)), self.readExcel(57, 1), self.readExcel(57, 2))
        self.assertEqual(u'区信息维护', self.getTitleInfo())

    def test_027(self):
        '''验证省编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseRegion()
        self.createArea(int(self.readExcel(58, 0)), self.readExcel(58, 1), self.readExcel(58, 2))
        self.assertEqual(u'区信息维护', self.getTitleInfo())



if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Region))
    unittest.TextTestRunner(verbosity=2).run(suite)