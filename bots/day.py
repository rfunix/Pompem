#!/usr/bin/python
# -*- coding: utf-8 -*-

from model.result import Result
from bots.bot_base import Base
import re
import sys


class BotDay(Base):

    def __init__(self):
        Base.__init__(self)

    def bot_search(self):
        self.results = []
        url = "http://1337day.com/search"
        data = {"search_request": "{0}".format(
            self.filter_description),
            "search_type": "1",
            "category": "-1",
            "plataform": "-1",
            "price_from": "0",
            "price_to": "10000",
            "author_login": "",
            "cve": ""}
        try:
            pagehtml = self.object_download.post_download_page_day(url, data)
            if (pagehtml):
                self.extract_data(pagehtml)
        except Exception, ex:
            pass
        return self.results

    def extract_data(self, html):
        html = str(html).replace("\n", " ")
        html = re.sub(r"\"", "'", html)
        r = re.compile(r"<tr.*?<td class='date'>(?P<Date>\d{4}-\d{2}-\d{2}).*?"
                       "<td class='dlink'>.*?<a href='(?P<Download>[^']*?)'.*?"
                       "description.*?<a[^>]*?>(?P<Description>[^<]*?)<.*?author.*?"
                       "title='(?P<Author>[^']*?')")
        for match in r.finditer(html):
            if match:
                self.results.append(match.groupdict())
                numDownload = re.search(
                    r"\d+?$", self.results[len(self.results) - 1]['Download'])
                self.results[len(self.results) - 1]['Download'] = \
                    "http://1337day.com/exploit/{0}".format(
                        numDownload.group(0))