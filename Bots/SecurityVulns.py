# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
from Engine.Functions import DownloadPage
from Model.Result import Result

import re

class SecurityVulns:
    def __init__(self, filter_description=None, results=[],):
        self.filter_description = filter_description
        self.results = results

    def botSearch(self):
        d = DownloadPage()
        self.results = []
        url = "http://securityvulns.com/exploits/"
        parameters = {"keyword":"{0}".format(self.filter_description),}
        try:
            pagehtml = d.getDownloadPage(url, parameters)
            if (pagehtml):
                self.extractData(pagehtml)
        except Exception, ex:
            pass
        return self.results



    def extractData(self, html):
        result = Result()
        html = re.sub(r"\n", "", html)
        html = re.sub(r"\"", "'", html)
        r = re.compile(r"(?i)<td bgcolor='[^']*?'.*?a class='tiny' href='([^']*?)'>([^<]*?)<")
        for match in r.finditer(html):
            if match:
                if not "search" in str(match.group(1)):
                    dictResult = {}
                    dictResult["Download"] = "http://securityvulns.com{0}".format(match.group(1))
                    dictResult["Description"] = match.group(2)
                    dictResult["Date"] = "0000-00-00"
                    dictResult["Author"] = "undefined"
                    dictResult["Link"] = "undefined"
                    self.results.append(dictResult)
