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
        for i in range(5):
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
        html = re.sub(r"\"", "'", html)
        r = re.search(r"(?ms)<form action='/search/' method='get'.*?<div id='nv'", html)
        html = r.group()
        html = re.sub(r"\n", " ", html)

        r2 = re.compile(r"<dl id='[^']*' class='[^']*?'>.*?"
                        "title='[^']*?'>(?P<Description>[^<]*?)<.*?"
                        "href='.*?(?P<Date>\d{4}-\d{2}-\d{2}).*?"
                        "'person'>(?P<Author>[^<]*?)</a>.*?"
                        "/files/tags/exploit.*?"
                        "act-links'><a href='(?P<Download>[^']*?)'")

        r = re.compile("<dl.*?</dl>")
        for match in r.finditer(html):
            match2 = r2.search(match.group())
            if match2:
                self.results.append(match2.groupdict())
                self.results[len(self.results) -1]['Download'] = \
                    "http://packetstormsecurity.com{0}".format(self.results[len(self.results) -1]['Download'])







