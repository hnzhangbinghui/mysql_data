import os
import pymysql
import unittest
import xlrd
import HTMLTestRunner


class testCompare(unittest.TestCase):
    def setUp(self):
        self.filename = "Lenovo.xlsx"
        self.filepath = os.path.join(os.getcwd(), self.filename)
        self.excel_file = xlrd.open_workbook(self.filepath)
        self.sheet = self.excel_file.sheet_by_index(0)
        self.targets_excel = self.sheet.col_values(6, 1)
        return self.targets_excel

    def test_Open_data(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='zbh123456', port=3306, database='world')
        self.cur = self.conn.cursor()
        sql = 'SELECT * FROM zhang_lenovo'
        self.count = self.cur.execute(sql)
        self.all_data = self.cur.fetchall()
        self.targets_data = []
        for i in range(self.count):
            self.targets_data.append(int(self.all_data[i][6]))
        return  self.targets_data

    def test_Compare_data(self):
        self.tar_excel = self.setUp()
        self.tar_data = self.test_Open_data()
        for i in range(len(self.tar_excel)):
            if self.tar_excel[i] == self.tar_data[i]:
                print("Calculation rasult is True!!")
            else:
                #self.test_Open_incentiveID(i)
                print("数据库的值是：", self.tar_data[i], " ", "excel表格的值是：", self.tar_excel[i])
                self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='zbh123456', port=3306, database='world')
                self.cur = self.conn.cursor()
                self.sql = 'SELECT * FROM zhang_lenovo'
                self.count = self.cur.execute(self.sql)
                self.assert_data = self.cur.fetchall()
                self.assert_data = list(self.assert_data)
                print("该incentiveID的值是：%s", self.assert_data[i][3])

'''  def test_Open_incentiveID(self, *x):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', passwd='zbh123456', port=3306, database='world')
        self.cur = self.conn.cursor()
        self.sql = 'SELECT * FROM zhang_lenovo'
        self.count = self.cur.execute(self.sql)
        self.assert_data = self.cur.fetchall()
        self.assert_data=list(self.assert_data)
        print("该incentiveID的值是：%s",self.assert_data[x][3])'''


if __name__ == '__main__':
    import os
    filename = '20191124.html'
    filepath = os.path.join(os.getcwd(), filename)
    fp = open(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(testCompare('setUp'))
    suite.addTest(testCompare('test_Open_data'))
    suite.addTest(testCompare('test_Compare_data'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Lenovo Calculation Result")
    runner.run(suite)
    unittest.main()
