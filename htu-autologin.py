import time
import os
from selenium import webdriver
#先安装pywin32，才能导入下面两个包
import win32api
import win32con
#导入处理alert所需要的包
from selenium.common.exceptions import NoAlertPresentException
import traceback
while(1):
    backinfo = os.system('ping 220.181.38.149') # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
    if backinfo:  #未联网状态执行自动联网程序
        netstate = 1
    else:         #联网是执行循环扫描网络状态
        netstate = 0
    while(netstate):
        #环境配置
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application"
        os.environ["webdriver.ie.driver"] = chromedriver
        
        driver=webdriver.Chrome() # 选择Chrome浏览器
        driver.get('http://210.42.255.130/portalReceiveAction.do?wlanuserip=10.21.71.142&wlanacname=HNSFDX_H3C-S8808-X') # 打开网站，连接校园网自动跳出的地址。
        driver.maximize_window() #最大化谷歌浏览器
        #处理alert弹窗
        try:
            alert1 = driver.switch_to.alert #switch_to.alert点击确认alert
        except NoAlertPresentException as e:
            print("no alert")
            traceback.print_exc()
        else:
            at_text1 = alert1.text
            print("at_text:" + at_text1)
        
        time.sleep(1)
        
        #driver.find_element_by_link_text('登录').click() # 点击“账户登录”
        
        username = "******" # 请替换成你的用户名
        password = "******" # 请替换成你的密码
        
        driver.find_element_by_id('useridtemp').click() # 点击用户名输入框
        driver.find_element_by_id('useridtemp').clear() #清空输入框
        driver.find_element_by_id('useridtemp').send_keys(username) # 自动敲入用户名
        
        driver.find_element_by_id('passwd').click() # 点击密码输入框
        driver.find_element_by_id('passwd').clear() #清空输入框
        driver.find_element_by_id('passwd').send_keys(password) # 自动敲入密码

        driver.find_element_by_id('checkButton').click() # 点击“登录”
        
        #采用class定位登陆按钮
        # driver.find_element_by_class_name('checkButton').click() # 点击“登录”按钮
        #采用xpath定位登陆按钮，
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/form/button').click() 
        
        time.sleep(1)
        
        #driver.find_element_by_id('signIn').click() # 点击“签到”
        
        win32api.keybd_event(122,0,0,0)  #F11的键位码是122，按F11浏览器全屏
        win32api.keybd_event(122,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
        
        driver.close()
        netstate = 0
    time.sleep(7200)  #每过两个小时检测网络连接状态
