# -*- coding: utf-8 -*-
from threading import Thread
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from BeautifulSoup import BeautifulStoneSoup

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestWorker(Thread):
    def __init__(self, url, data=None, session_url=None):
        Thread.__init__(self)
        self._url = url
        self._html = None
        self._data = data
        self._session_url = session_url
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0'
        }
        if self._session_url:
            self._session = requests.session()
            self._request_session = self._session.post(self._session_url, data=self._data, headers=self._headers)
            self._response_sesssion = self._request_session.text

    def run(self):
        if self._session_url:
            req = self._session.get(self._url, verify=False, headers=self._headers)
        else:
            req = requests.get(self._url, verify=False, headers=self._headers)
        req.encoding = 'utf-8'
        decoded_html = BeautifulStoneSoup(
            req.text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
        self._html = str(decoded_html)

    def join(self):
        Thread.join(self)
        return self._html
