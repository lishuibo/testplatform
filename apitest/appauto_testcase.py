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

from apitest import config
from apitest import HTMLTestRunner
import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

HOSTNAME = '127.0.0.1'


def readSQLcase():
    sql = 'SELECT id,appfindmethod,appevelement,appoptmethod,appassertdata,apptestresult from apptest_appcasestep WHERE apptest_appcasestep.appcase_id=1 ORDER BY id ASC;'
    conn = pymysql.connect(user='root', passwd='123456', db='autotest', port=3306,
                           host=config.getConfig("database", "host"), charset='utf8')
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
            driver.find_element_by_id(evelement).send_keys('wayto')
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            driver.find_element_by_name(evelement).click()
        elif optmethod == 'sendkey':
            driver.find_element_by_name(evelement).send_keys()


if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'emulator-5554'
    desired_caps['appPackage'] = 'com.android.test'
    desired_caps['appActivity'] = '.Test'
    desired_caps['app'] = PATH('D:\\android-sdk-windows\\platform-tools\\csdn.apk')

    time.sleep(1)
    driver = webdriver.Remote('http://127.0.0.1/wd/hub', desired_caps)
    time.sleep(1)
    readSQLcase()
    driver.quit()
    print('Done!')
    time.sleep(1)