# _*_ coding:utf-8 _*_
 
#author:PJL
 
#ubuntu+python2.7.x
 
import urllib2
import sys
import re
import sqlite3
from bs4 import BeautifulSoup
 
def jingdong(url,keyword):
    page = urllib2.urlopen(url)
    html_doc = page.read()
    soup = BeautifulSoup(html_doc.decode('utf-8','ignore'))
    print soup
    cx = sqlite3.connect("/home/pengjialing/git/test.db")
    cu = cx.cursor()
    cu.execute('drop table if exists '+keyword)
    cu.execute('create table if not exists '+keyword+' (id integer primary key, nid varchar(20), name varchar(50), price decimal(18,2))')
    for i in soup.find_all('script'):
        string = i.get_text()
        # print string
        # namelist = re.findall(ur'"raw_title":"[^\"]+"', string)
        # nidlist = re.findall(r'"nid":"\d+"', string)
        # pricelist = re.findall(r'"view_price":"\d+\.?\d+"', string)
        # if nidlist:
        #     for j in range(len(nidlist)):
        #                 name = namelist[j].split("\"")[3]
        #         nid = nidlist[j].split("\"")[3]
        #                 price = pricelist[j].split("\"")[3]
        #                 cu.execute('insert into '+keyword+' (nid, name, price) values (?, ?, ?)', (nid,name,price))
    cx.commit()
    cx.close()


 
keyword = sys.argv[1]
jingdong("http://search.jd.com/Search?keyword="+keyword+"&enc=utf-8",keyword)