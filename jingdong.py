# _*_ coding:utf-8 _*_
 
#author:PJL
 
#ubuntu+python2.7.x
 
import urllib2
import sys
import re
import sqlite3
from bs4 import BeautifulSoup
 
def jingdong(keyword):
    cx = sqlite3.connect("/home/pengjialing/git/test.db")
    cu = cx.cursor()
    cu.execute('drop table if exists jd_'+keyword)
    cu.execute('create table if not exists jd_'+keyword+' (id integer primary key, nid varchar(30), name varchar(50), price decimal(18,2))')
    for i in range(5):
        url = "http://search.jd.com/Search?keyword="+keyword+"&enc=utf-8"
        page = urllib2.urlopen(url)
        html_doc = page.read()
        soup = BeautifulSoup(html_doc.decode('utf-8','ignore'))
        for i in soup.find_all(attrs={'class':'p-price'}):
            nid = i.contents[1]['class'][0]
            price = float(i.contents[1].contents[1].get_text())
            d = i.find_next_sibling('div')
            em = d.find('em')
            name = em.get_text()
            cu.execute('insert into jd_'+keyword+' (nid, name, price) values (?, ?, ?)', (nid,name,price))
    cx.commit()
    cx.close()

keyword = sys.argv[1]
jingdong(keyword)