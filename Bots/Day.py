# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '..')
from Engine.Functions import DownloadPage
from Model.Result import Result

import re


class BotDay:
    def __init__(self, filter_description=None, results=[],):
        self.filter_description = filter_description
        self.results = results

    def botSearch(self):
        d = DownloadPage()
        self.results = []
        url = "http://1337day.com/search"
        data = {"dong": "{0}".format(self.filter_description), "submit_search": "Submit"}
        try:
            pagehtml = d.postDownloadPageDay(url, data)
            if (pagehtml):
                self.extractData(pagehtml)
        except Exception, ex:
            pass
        return self.results

    def extractData(self, html):
        result = Result()
        html = str(html).replace("\n", " ")
        html = re.sub(r"\"", "'", html)
        r = re.compile(r"<tr class='TableContent'>.*?>"
                        "(?P<Date>\d{4}-\d{2}-\d{2})"
                        "</a>.*?href='(?P<Download>[^']*?)'>.*?>"
                        "(?P<Description>[^<]*?)"
                        "<.*?free.*?author.*?>(?P<Author>[^<]*?)<")
        for match in r.finditer(html):
            if match:
                self.results.append(match.groupdict())
                numDownload = re.search(r"\d+?$", self.results[len(self.results)-1]['Download'])
                self.results[len(self.results) -1]['Download'] = \
                    "http://1337day.com/exploit/{0}".format(numDownload.group(0))









