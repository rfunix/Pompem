# -*- coding: utf-8 -*-

from model.result import Result
from bots.bot_base import Base 
import re



class BotDay(Base):
    def __init__(self):
        Base.__init__(self)

    def bot_search(self):
        self.results = []
        url = "http://1337day.com/search"
        data = {"dong": "{0}".format(self.filter_description), "submit_search": "Submit"}
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
