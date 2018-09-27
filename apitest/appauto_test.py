__author__ = 'Administrator'
import os
import time
import unittest
from selenium import webdriver

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
global driver


class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['devices'] = 'android'
        desired_caps['platform'] = 'Android'
        desired_caps['browserName'] = ''
        desired_caps['version'] = '4.4'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['app'] = PATH('D:\\android-sdk-windows\\platform-tools\\csdn.apk')
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

    def test_login(self):
        time.sleep(10)
        identity = self.driver.find_element_by_name('输入CSDN账号').send_keys("test")
        usn = self.driver.find_element_by_name('输入密码')
        usn.click()
        usn.send_keys("test2")
        self.driver.find_element_by_name('登录').click()
        time.strftime(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
