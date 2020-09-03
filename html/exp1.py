#-*- coding utf-8  -*-
'''
   просто игрушка
'''
import sys
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def GetPage(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'lxml')
    except:
        return None
    return bsObj

def getTitle(Page):
    title = Page.body.h1
    return title

def func(arg):
    if arg:
        return('href' in arg)
    else:
        return False

if __name__=="__main__":

    url = 'file://localhost//d://py//expr//test.html'
    url = "http://www.pythonscraping.com/pages/page1.html"
    url = "file:test.html"

    bsPage=GetPage(url)
    title = getTitle(bsPage)

    if title == None:
        print("Title could not be found")
    else:
        print(title)

    records=bsPage.find_all("a", func)
    print(len(records))
    for r in records:
        print(r)

else:
    pass

