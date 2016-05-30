#coding:utf-8
import unittest
from Model.BaseSet import Helper
from Model.baseNumber import DataHlper
from ways.wms import wmsPage


class Wms(Helper, DataHlper, wmsPage):

    def test001(self):
        '''验证只输入用户名是否登录成功'''
        self.typeUsername(self.readFile(1))
        self.loginButton()
        self.assertEqual(u'密码不能为空', self.get_prompt())

    def test002(self):
        '''验证只输入密码，是否登录成功'''
        self.typePassword(self.readFile(2))
        self.loginButton()
        self.assertEqual(u'登录名不能为空', self.get_prompt())

    def test003(self):
        '''验证用户名和密码正确登录'''
        self.login(self.readFile(1), self.readFile(2))
        self.assertEqual(u'欢迎使用WMS', self.get_title())

    def test004(self):
        '''验证登录后，可以正常退出'''
        self.login(self.readFile(1), self.readFile(2))
        self.exitLogin()


if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(Wms))
    unittest.TextTestRunner(verbosity=2).run(suite)