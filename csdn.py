#By:Tanck
import urllib2
import urllib
import math


for i in range(10000): #read times
    url = 'http://blog.csdn.net/u010316858/article/details/49300851' #your url
    req = urllib2.Request(url, headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    oper = urllib2.urlopen(req)
    print "currentTimes:",i+1
print("over")