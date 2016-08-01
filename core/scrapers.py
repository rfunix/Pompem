#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
import datetime
import re
from core.request_worker import RequestWorker


class Scraper(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.list_result = None
        self.list_req_workers = []

    def parser(self):
        raise NotImplementedError()

    def join(self):
        Thread.join(self)
        return self.list_result


class PacketStorm(Scraper):
    def __init__(self, key_word):
        Scraper.__init__(self)
        self.name_site = "Packet Storm Security"
        self.name_class = PacketStorm.__name__
        self.base_url = "https://packetstormsecurity.com"
        self.key_word = key_word
        self.url = "https://packetstormsecurity.com/search/files/page{0}/?q={1}"
        self.page_max = 2
        self.list_result = []
        self.regex_item = re.compile(r'(?ms)(<dl id="[^"]*?".*?<\/dl>)')
        self.regex_url = re.compile(r'href="(/files/\d+?\/[^"]*?)"')
        self.regex_date = re.compile(r'href="/files/date/(\d{4}-\d{2}-\d{2})')
        self.regex_name = re.compile(r'href="/files/\d+?\/[^"]*?".*?title.*?>([^<]*?)<')

    def run(self, ):
        for page in range(self.page_max):
            try:
                url_search = self.url.format(page + 1, self.key_word)
                req_worker = RequestWorker(url_search)
                req_worker.start()
                self.list_req_workers.append(req_worker)
            except Exception, e:
                import traceback
                print  traceback.print_exc()
        self._get_results()

    def _get_results(self):
        for r_worker in self.list_req_workers:
            try:
                html = r_worker.join()
                self._parser(html)
            except Exception, e:
                import traceback
                print traceback.print_exc()

    def join(self):
        Thread.join(self)
        return self.list_result

    def _parser(self, html):
        for item in self.regex_item.finditer(html):
            item_html = item.group(0)
            dict_result = {}
            url_exploit = "{0}{1}".format(
                self.base_url,
                self.regex_url.search(item_html).group(1)
            )
            dict_result['url'] = url_exploit
            dict_result['date'] = self.regex_date.search(item_html).group(1)
            dict_result['name'] = self.regex_name.search(item_html).group(1)
            self.list_result.append(dict_result)


class CXSecurity(Scraper):
    def __init__(self, key_word):
        Scraper.__init__(self)
        self.name_site = "CXSecurity"
        self.name_class = CXSecurity.__name__
        self.key_word = key_word
        self.url = "https://cxsecurity.com/search/wlb/DESC/AND/{0}.1999.1.1/{1}/10/{3}/"
        self.page_max = 2
        self.list_result = []
        self.regex_item = re.compile(r'(?msi)<tr>.*?<td width="17".*?<td width="550".*?</tr>')
        self.regex_url = re.compile(r'(?msi)<td.*?<h6><a href="([^"]*?)"')
        self.regex_date = re.compile(r'(?msi)<td width="80".*?default">(\d{2})\.(\d{2})\.(\d{4})')
        self.regex_name = re.compile(r'(?msi)title="([^"]*?)"')

    def run(self, ):
        now_date = '{dt.year}.{dt.month}.{dt.day}'.format(
            dt=datetime.datetime.now()
        )
        for page in range(self.page_max):
            try:
                url_search = self.url.format(now_date, page + 1, self.page_max,
                                             self.key_word)
                req_worker = RequestWorker(url_search)
                req_worker.start()
                self.list_req_workers.append(req_worker)
            except Exception, e:
                import traceback
                print  traceback.print_exc()
            self._get_results()

    def _get_results(self):
        for r_worker in self.list_req_workers:
            try:
                html = r_worker.join()
                self._parser(html)
            except Exception, e:
                import traceback
                print traceback.print_exc()

    def join(self):
        Thread.join(self)
        return self.list_result

    def _parser(self, html):
        for item in self.regex_item.finditer(html):
            item_html = item.group(0)
            dict_result = {}
            url_exploit = self.regex_url.search(item_html).group(1)
            dict_result['url'] = url_exploit
            match_date = self.regex_date.search(item_html)
            date = "{0}-{1}-{2}".format(match_date.group(3),
                                        match_date.group(2),
                                        match_date.group(1)
                                        )
            dict_result['date'] = date
            dict_result['name'] = self.regex_name.search(item_html).group(1)
            self.list_result.append(dict_result)
