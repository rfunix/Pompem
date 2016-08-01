# -*- coding: utf-8 -*-
from threading import Thread
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from BeautifulSoup import BeautifulStoneSoup

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestWorker(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self._url = url
        self._html = None

    def run(self):
        req = requests.get(self._url, verify=False)
        req.encoding = 'utf-8'
        decoded_html = BeautifulStoneSoup(
            req.text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
        self._html = str(decoded_html)

    def join(self):
        Thread.join(self)
        return self._html
