# -*- coding: UTF-8 -*-

import requests
import sys
from BeautifulSoup import BeautifulStoneSoup
sys.path.insert(0, '..')


class DownloadPage(object):
    def __init__(self, url=None):
        self.url = url

    def getDownloadPage(self, host, parametros):
        try:
            headers = {'User-Agent': 'Googlebot '}

            r = requests.get(host, params=parametros, headers=headers)

            decodedstring = BeautifulStoneSoup(r.text,
                                              convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
            return str(decodedstring)
        except Exception, e:
            print (e.message)
            return None

        def getUrlPageDownload(self, host, parametros):
            try:
                headers = {'User-Agent': 'Googlebot '}

                r = requests.get(host, params=parametros, headers=headers)

                return r.url()
            except Exception, e:
                print (e.message)
                return None