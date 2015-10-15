#-*- coding: cp949-*-
'''
Created on 2012. 7. 4.
@author: KIM SUN GHU
각 os 별  Browser실 행  및 surffing 하도록 구현
특히 page의 a tag를 검출 하여 랜덤으로  url을  browser에 던짐
'''
import os  # 'posix', 'nt', 'os2', 'ce', 'java', 'riscos'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class InetBrowser():
    def __init_(self):
        self.OsName = os.name 
        if "posix" == self.OsName:
            self.browser = webdriver.Firefox() # Get local session of firefox
        elif "nt" == self.OsName:
            self.browser = webdriver.Ie() # Get local session of internet explorer
        elif "mac" == self.OsName:
            self.browser = webdriver.Chrome() #

    def __del__(self):
        self.browser.close()
                    
    def GoToURL(self,url="http://www.ted.com"):
        self.browser.get(url) # Load page
        
    def GetAtagList(self,srvurl):
       
       # assert "Yahoo!" in browser.title
        elem = browser.find_element_by_name("p") # Find the query box
        elem.send_keys("seleniumhq" + Keys.RETURN)
        time.sleep(0.2) # Let the page load, will be added to the API
        try:
            browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
            except NoSuchElementException:
                assert 0, "can't find seleniumhq"
                browser.close()