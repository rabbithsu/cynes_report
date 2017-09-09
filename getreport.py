# -*- coding: utf-8 -*- 

from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys 

from bs4 import BeautifulSoup
from datetime import *
import time 
import os 
import urllib, urllib2
import codecs

#start = date(2013, 01, 25)
#end = date(2015, 01, 01)
#day = timedelta(1)
#now = start

month = 8
end = 9

browser = webdriver.Chrome('chromedriver') 
browser.implicitly_wait(20)
searchurl = "http://www.cnyes.com/report/rsh_list.aspx?ga=nav"
logf = codecs.open("log_report.txt", "a", "utf-8")
browser.get(searchurl)

while(month != end):
	#search 1 month data
	start = browser.find_element_by_id("ctl00_ContentPlaceHolder1_tbx_StartDate")
	start.clear()
	start.send_keys("2015-0"+str(month) + "-01")
	ed = browser.find_element_by_id("ctl00_ContentPlaceHolder1_tbx_EndDate")
	ed.clear()
	ed.send_keys("2015-0"+str(month+1) + "-01")
	browser.find_element_by_id("ctl00_ContentPlaceHolder1_btn_Search").click()
	time.sleep(10)

	save = ""
	count = 0
	#get total page number
	page = browser.find_element_by_id("ctl00_ContentPlaceHolder1_LastPaeg")
	tmp = page.get_attribute("href")
	pn = int(tmp.split("=")[1].split("&")[0])

	for i in range(pn) :
		try:
			browser.get("http://www.cnyes.com/report/rsh_list.aspx?page=" + str(i+1) + "&ga=nav")
			time.sleep(5)
			links = browser.find_elements_by_xpath('//table/tbody/tr/td/a')
			for url in links:
				save = save + "http://www.cnyes.com/report/"+ url.get_attribute("href") +"\n"
				count += 1

		except:
			save += "can't load page.\n"
			break;

	fn = os.path.join(os.path.dirname(__file__), "downloads_report", str(month) +".txt")
	f = codecs.open(fn, "w+", "utf-8")
	f.write(save)
	f.close()
	logf.write(time.strftime('%Y-%m-%d %H:%M:%S'))
	logf.write(":  file "+ str(month) + ".txt finished.   " + str(count) + " links added.\n")
	month += 1
	time.sleep(2)
logf.close()
	






