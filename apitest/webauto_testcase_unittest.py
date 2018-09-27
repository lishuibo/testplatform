__author__ = 'Administrator'
import os
import time
import unittest
from selenium import webdriver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
global driver

import requests, time, sys, re
import urllib, zlib
import pymysql

from apitest import HTMLTestRunner
import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

HOSTNAME = '127.0.0.1'


class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.baidu.com")
        time.sleep(1)

    def test_readSQLcase1(self):
        sql = 'SELECT id,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata,webtestresult from webtest_webcasestep WHERE webtest_webcasestep.webcase_id=1 ORDER BY id ASC ;'
        conn = pymysql.connect(user='root', passwd='123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
        cursor = conn.cursor()
        aa = cursor.execute(sql)
        info = cursor.fetchmany(aa)

        for i in info:
            case_list = []
            case_list.append(i)
            webtestcase(case_list)

        conn.commit()
        cursor.close()
        conn.close()

    def test_readSQLcase2(self):
        sql = 'SELECT id,webfindmethod,webevelement,weboptmethod,webtestdata,webassertdata,webtestresult from webtest_webcasestep WHERE webtest_webcasestep.webcase_id=1 ORDER BY id ASC ;'
        conn = pymysql.connect(user='root', passwd='123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
        cursor = conn.cursor()
        aa = cursor.execute(sql)
        info = cursor.fetchmany(aa)

        for i in info:
            case_list = []
            case_list.append(i)
            webtestcase(case_list)

        conn.commit()
        cursor.close()
        conn.close()

    def tearDown(self):
        self.driver.quit()


def webtestcase(case_list):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[1]
            evelement = case[2]
            optmethod = case[3]
            testdata = case[4]
        except Exception as e:
            return '测试用例格式不正确%s' % e
        print(evelement)
        time.sleep(10)

        if optmethod == 'sendkyes' and findmethod == 'find_element_by_id':
            driver.find_element_by_id(evelement).send_keys(testdata)
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            driver.find_element_by_name(evelement).click()
        elif optmethod == 'click' and findmethod == 'find_element_by_id':
            driver.find_element_by_id(evelement).click()


if __name__ == '__main__':
    time.sleep(1)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Search("test_readSQLcase1"))
    testunit.addTest(Search("test_readSQLcase2"))

    filename = "F:\\pycharmwork\\autotest\\report\\" + "webtest_report.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"web自动化测试报告", description=u"web自动化测试")
    runner.run(testunit)
    print('Done!')
    time.sleep(1)