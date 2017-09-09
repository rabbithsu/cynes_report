#encoding: utf-8
from bs4 import BeautifulSoup
import urllib, urllib2
import re
import time
import os
import codecs

for i in range (446):
	save = ""
	count = 198735
	url = urllib2.urlopen("http://www.cnyes.com/report/rsh_article.aspx?id=" + str(count+i))
	soup = BeautifulSoup(url, 'html.parser')
	title = soup.h1.string.replace(" ", "").replace("\n", "").replace("\r","")
	print title
	if title == "":
		continue
	subtitle = (soup.find(id="searchform").text).replace("\"", "").replace(" ", "").replace(u'\xa0', "").replace("\r", "").replace("\n", " ")
	print subtitle
	match = re.search("\d\d\d\d-\d\d-\d\d", subtitle)
	date = match.group()
	save = title + "\n" + subtitle + "\n\n"
	title = title.replace("?", u"？")
	title = title.replace("/", u"／")
	fn = os.path.join(os.path.dirname(__file__), "downloads", date+title+".txt")
	f = codecs.open(fn, "w+", "utf-8")
	for dlink in soup.find_all("p", attrs={'class': None}):
		if not dlink.a:
			if not dlink.string:
				save += ""
			else:
				save = save + dlink.string
	f.write(save)
	f.close()
	time.sleep(1)
	#193929 198735 199180 
