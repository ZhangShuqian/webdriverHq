#coding:utf-8
import unittest
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.Systest import SysPage
from ways.wms import wmsPage


class Customer(Helper, DataHlper, wmsPage, SysPage):
    def test_001(self):
        '''验证不点击全选，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.clickBatchCustomer()
        self.clickEndCustomer()
        self.assertEqual(u'请选择需要停用的客户', self.getPrompt())

    def test_002(self):
        '''验证不点击全选，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.clickBatchCustomer()
        self.clickStartCustomer()
        self.assertEqual(u'请选择需要启用的客户', self.getPrompt())

    def test_003(self):
        '''验证客户编码为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(10, 0), self.readExcel(10, 1), self.readExcel(10, 2), self.readExcel(10, 3),
                            int(self.readExcel(10, 4)), int(self.readExcel(10, 5)), int(self.readExcel(10, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_004(self):
        '''验证客户名称为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(11, 0), self.readExcel(11, 1), self.readExcel(11, 2), self.readExcel(11, 3),
                               int(self.readExcel(11, 4)), int(self.readExcel(11, 5)), int(self.readExcel(11, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_005(self):
        '''验证联系人为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(12, 0), self.readExcel(12, 1), self.readExcel(12, 2), self.readExcel(12, 3),
                               int(self.readExcel(12, 4)), int(self.readExcel(12, 5)), int(self.readExcel(12, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_006(self):
        '''验证联系电话为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(13, 0), self.readExcel(13, 1), self.readExcel(13, 2), self.readExcel(13, 3),
                               int(self.readExcel(13, 4)), int(self.readExcel(13, 5)), int(self.readExcel(13, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_007(self):
        '''验证结算方式为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(14, 0), self.readExcel(14, 1), self.readExcel(14, 2),
                               self.readExcel(14, 3),
                               int(self.readExcel(14, 4)), int(self.readExcel(14, 5)), int(self.readExcel(14, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_008(self):
        '''验证发票类型为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(15, 0), self.readExcel(15, 1), self.readExcel(15, 2),
                               self.readExcel(15, 3),
                               int(self.readExcel(15, 4)), int(self.readExcel(15, 5)), int(self.readExcel(15, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_009(self):
        '''验证客户类型为空，是否可以保存'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.createCustomerButton()
        self.createCustomer(self.readExcel(16, 0), self.readExcel(16, 1), self.readExcel(16, 2),
                               self.readExcel(16, 3),
                               int(self.readExcel(16, 4)), int(self.readExcel(16, 5)), int(self.readExcel(16, 6)))
        self.assertEqual(u'客户信息维护', self.getTitleCustomer())

    def test_010(self):
        '''验证勾选客户，是否可以批量停用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.clickBatchCustomer()
        self.clickAllSelectCustomer()
        self.clickBatchCustomer()
        self.clickEndCustomer()
        self.assertEqual(u'停用', self.getStateCustomer())

    def test_011(self):
        '''验证勾选客户，是否可以批量启用'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.clickBatchCustomer()
        self.clickAllSelectCustomer()
        self.clickBatchCustomer()
        self.clickStartCustomer()
        self.assertEqual(u'启用', self.getStateCustomer())

    def test_012(self):
        '''验证单个停用customer'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.clickSingleEditCustomerButton()
        self.clickSingleEndCustomer()
        self.assertEqual(u'停用', self.getStateCustomer())

    def test_013(self):
        '''验证单个启用customer'''
        self.login(self.readFile(1), self.readFile(2))
        self.clickBaseMenue()
        self.clickBaseCustomer()
        self.clickSingleEditCustomerButton()
        self.clickSingleStartCustomer()
        self.assertEqual(u'启用', self.getStateCustomer())


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Customer))
    unittest.TextTestRunner(verbosity=2).run(suite)