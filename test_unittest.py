import unittest
import sys
from myfunc import is_prime,add,divide

from HtmlTestRunner import HTMLTestRunner
#导入第三方htmltestrunner模块，执行结果生成html报告；安装方式：pip install html-testRunner

class TestMyFunc(unittest.TestCase):

    '''def setUp(self):
        print("每个用例执行前会调用setUp方法准备环境")
    def tearDown(self):
        print("每个用例执行后会调用tearDown方法进行环境清理")'''
    #全部的用例使用一次setUp和tearDown
    @classmethod
    def setUpClass(cls):
        print("所有用例执行前会调用一次setUp准备环境")
    @classmethod
    def tearDownClass(cls):
        print("所有用例执行后会调用一次tearDown进行环境清理")

    def test_is_prime(self):
        print("测试is_prime方法")
        #测试用例以test_开头；使用unittest提供的断言方法；
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(5))
        #self.assertTrue(is_prime(0))
        #self.assertTrue(is_prime(1))
        #self.assertTrue(is_prime(-3))

    def test_add(self):
        print("测试add方法")
        self.assertEqual(3,add(2,1))
        self.assertEqual(4,add(2,2))

    @unittest.skipUnless(sys.platform.startswith("linux"),"requires linux") #跳过此用例
    def test_divide(self):
        print("测试divide方法")
        self.assertEqual(2,divide(6,3))
        self.assertEqual(2,divide(4,2))

if __name__=='__main__':
    unittest.main()
    #注意观察用例的执行顺序；注意观察setUp和teardown的执行；跳过用例，输出html报告；

    #使用testsuite来控制用例的执行的顺序；
    tests=[TestMyFunc("test_is_prime"),TestMyFunc("test_add"),TestMyFunc("test_divide")]

    suite=unittest.TestSuite()  #实例化套件

    suite.addTests(tests) #将测试用例实例增加到测试套件
    '''runner=unittest.TextTestRunner()
    runner.run(suite)'''
    runner=HTMLTestRunner(output='result')
    runner.run(suite)