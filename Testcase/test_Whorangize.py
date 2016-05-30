#coding:utf-8
import unittest
import time
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.warehouseSet import WarePage
from ways.wms import wmsPage


class Orangize(Helper, DataHlper, wmsPage, WarePage):
    def test001(self):
        '''验证系统登录后，默认的组织'''
        self.login(self.readFile(1), self.readFile(2))
        self.assertEqual(u'集团', self.getOrangizeName())

    def test002(self):
        '''验证是否切可以切换组织'''
        self.login(self.readFile(1), self.readFile(2))
        self.changeOrangize()
        time.sleep(1)
        self.assertEqual(u'test仓', self.getOrangizeName())

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Orangize))
    unittest.TextTestRunner(verbosity=2).run(suite)