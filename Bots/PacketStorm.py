# -*- coding: UTF-8 -*-
import sys
sys.path.insert(0, '..')
from Engine.Functions import DownloadPage
from Model.Result import Result

import re


class PacketStorm:
    def __init__(self, filter_description=None, results=[]):
        self.filter_description = filter_description
        self.results = results

    def botSearch(self):
        d = DownloadPage()
        self.results = []
        for i in range(2):
            url = "http://packetstormsecurity.com/search/files/page{0}/".format(i)
            parameters = {"q": "{0}".format(self.filter_description)}
            try:
                pagehtml = d.getDownloadPage(url, parameters)
                if (pagehtml):
                    self.extractData(pagehtml)
            except Exception, ex:
                pass
        return self.results



    def extractData(self, html):
        result = Result()
        html = re.sub(r"\n", " ", html)
        html = re.sub(r"\"", "'", html)
        r = re.compile(r"<dl id='[^']*' class='[^']*?'>.*?"
                        "title='[^']*?'>(?P<Description>[^<]*?)<.*?"
                        "href='.*?(?P<Date>\d{4}-\d{2}-\d{2}).*?"
                        "'person'>(?P<Author>[^<]*?)</a>.*?"
                        "/files/tags/exploit.*?"
                        "act-links'><a href='(?P<Download>[^']*?)'")
        for match in r.finditer(html):
            if match:
                self.results.append(match.groupdict())
                self.results[len(self.results) -1]['Download'] = \
                    "http://packetstormsecurity.com{0}".format(self.results[len(self.results) -1]['Download'])








