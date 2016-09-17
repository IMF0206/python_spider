# _*_ coding:utf-8 _*_
 
#author:PJL
 
#ubuntu+python2.7.x
 
import urllib2
import sys
import re
from bs4 import BeautifulSoup
 
def taobao(url):
    page = urllib2.urlopen(url)
    html_doc = page.read()
    soup = BeautifulSoup(html_doc.decode('utf8','ignore'))
    for i in soup.find_all('script'):
        string = i.get_text()
        one = re.findall(r'"nid":"\d+"', string)
        if one:
        	for j in one:
        		nid = j.split("\"")[3]
        		print nid
 
keyword = sys.argv[1]
taobao("https://s.taobao.com/search?q="+keyword)