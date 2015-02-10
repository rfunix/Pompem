# -*- coding: utf-8 -*-

from model.result import Result
from bots.bot_base import Base
import re


class PacketStorm(Base):
    def __init__(self):
        Base.__init__(self)

    def bot_search(self):
        self.results = []
        for i in range(5):
            url = "http://packetstormsecurity.com/search/files/page{0}/".format(i)
            parameters = {"q": "{0}".format(self.filter_description)}
            try:
                pagehtml = self.object_download.getDownloadPage(url, parameters)
                if (pagehtml):
                    self.extract_data(pagehtml)
            except Exception, ex:
                pass
        return self.results

    def extract_data(self, html):
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







