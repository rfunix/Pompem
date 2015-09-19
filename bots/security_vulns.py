#!/usr/bin/python
# -*- coding: utf-8 -*-

from model.result import Result
from bots.bot_base import Base
import re


class SecurityVulns(Base):
    def __init__(self):
        Base.__init__(self)

    def bot_search(self):
        self.results = []
        url = "http://securityvulns.com/exploits/"
        parameters = {"keyword":"{0}".format(self.filter_description),}
        try:
            pagehtml = self.object_download.get_download_page(url, parameters)
            if (pagehtml):
                self.extract_data(pagehtml)
        except Exception, ex:
            pass
        return self.results

    def extract_data(self, html):
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
