#coding:utf-8
import os, xlrd, unittest
class Config(object):
    def __init__(self):
        pass

    @staticmethod
    def data_dirs():
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DATA_DIRS = os.path.join(BASE_DIR, 'Data_Driven')
        # d = '/'.join(DATA_DIRS)
        return DATA_DIRS

    @staticmethod
    def testcase_dirs():
        Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Data_dir = os.path.join(Base_dir, 'Testcase')
        # d = '/'.join(Data_dir)
        return Data_dir

    @staticmethod
    def report_dirs():
        Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        Data_dir = os.path.join(Base_dir, 'report')
        return Data_dir


class DataHlper(object):
    def __init__(self):
        pass

    def readFile(self, index):
        f = open(Config.data_dirs() +  '/system.txt', 'r')
        d = f.readlines()
        f.close()
        return d[index]

    def readExcel(self, rowValue, colValue): #获取一行信息
        excel = xlrd.open_workbook(Config.data_dirs() + '/system.xlsx')
        sheet = excel.sheet_by_index(0)
        return sheet.cell_value(rowValue, colValue)

    def readExcels(self):   #读取整个sheet的数据
        rows = []
        excel = xlrd.open_workbook(Config.data_dirs() + '/system.xlsx')
        sheet = excel.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            rows.append(list(sheet.row_values(row, 0, sheet.ncols)))
        return rows

