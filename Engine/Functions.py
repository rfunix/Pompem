# -*- coding: UTF-8 -*-

import requests
import sys
import re
from BeautifulSoup import BeautifulStoneSoup
sys.path.insert(0, '..')


class DownloadPage(object):
    def __init__(self, url=None):
        self.url = url

    def getDownloadPage(self, host=None, parametros=None):
        try:
            headers = {'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html) '}

            r = requests.get(host, params=parametros, headers=headers)

            decodedstring = BeautifulStoneSoup(r.text,
                                              convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
            return str(decodedstring)
        except Exception, e:
            print (e.message)
            return None


    def postDownloadPagePacketStorm(self, host=None, postData={}):
        headers = {'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html) '}
        s = requests.session()
        s.post(host, headers=headers, data={"agree":"OK"})
        r = s.post(host,headers=headers, data=postData)


        decodedstring = BeautifulStoneSoup(r.text,
                                              convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

        return decodedstring
