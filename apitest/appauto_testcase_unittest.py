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


class Calculator(unittest.TestCase):
    def setUp(self):
        time.sleep(1)

    def test_readSQLcase(self):
        sql = 'SELECT id,appfindmethod,appevelement,appoptmethod,appassertdata,apptestresult from apptest_appcasestep WHERE apptest_appcasestep.appcase_id=1 ORDER BY id ASC ;'
        conn = pymysql.connect(user='root', passwd='123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
        cursor = conn.cursor()
        aa = cursor.execute(sql)
        info = cursor.fetchmany(aa)

        for i in info:
            case_list = []
            case_list.append(i)
            apptestcase(case_list)

        conn.commit()
        cursor.close()
        conn.close()

    def tearDown(self):
        time.sleep(1)


def apptestcase(case_list):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[1]
            evelement = case[2]
            optmethod = case[3]
        except Exception as e:
            return '测试用例格式不正确%s' % e
        print(evelement)
        time.sleep(10)

        if optmethod == 'click' and findmethod == 'find_element_by_id':
            driver.find_element_by_id(evelement).click()
            writeResult(case_id, '1')
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            driver.find_element_by_name(evelement).click()
            writeResult(case_id, '1')
        elif optmethod == 'sendkey':
            driver.find_element_by_name(evelement).send_keys('testdata')
            writeResult(case, '1')


def writeResult(case_id, result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apptest_appcasestep SET apptest_appcasestep.apptestresult=%s,apptest_appcasestep.create_time=%s WHERE apptest_appcasestep.apitest_id=%s;"
    param = (result, now, case_id)
    print('app autotest result is ' + result.decode())
    conn = pymysql.connect(user='root', passwd='123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    cursor.close()
    conn.close()


def caseWriteResult(case_id, result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apptest_appcase SET apptest_appcase.apptestresult=%s,apptest_appcase.create_time=%s WHERE apptest_appcase.id=%s;"
    param = (result, now, case_id)
    print('app autotest result is ' + result.decode())
    conn = pymysql.connect(user='root', passwd='123456', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'com.android.calculator2'
    desired_caps['appActivity'] = '.Calcculator'

    time.sleep(1)
    driver = webdriver.Remote('http://127.0.0.1/wd/hub', desired_caps)
    time.sleep(1)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Calculator("test_readSQLcase"))

    filename = "F:\\pycharmwork\\autotest\\report\\" + "apptest_report.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"app自动化测试报告", description=u"app自动化测试")
    runner.run(testunit)
    driver.quit()
    print('Done!')
    time.sleep(1)