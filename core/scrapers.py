#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from threading import Thread
import datetime
import re
from core.request_worker import RequestWorker, RequestWorkerHttpLib
import json


class Scraper(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.list_result = None
        self.list_req_workers = []

    def _parser(self):
        raise NotImplementedError()

    def join(self):
        Thread.join(self)
        return self.list_result

    def _get_results(self):
        for r_worker in self.list_req_workers:
            try:
                html = r_worker.join()
                self._parser(html)
            except Exception as e:
                import traceback
                traceback.print_exc()


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
            except Exception as e:
                import traceback
                traceback.print_exc()
        self._get_results()

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
            except Exception as e:
                import traceback
                traceback.print_exc()
        self._get_results()

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


class ZeroDay(Scraper):
    def __init__(self, key_word):
        Scraper.__init__(self)
        self.name_site = "ZeroDay"
        self.name_class = ZeroDay.__name__
        self.key_word = key_word
        self.url = "http://0day.today/search?search_request={0}"
        self.session_url = "http://0day.today"
        self.base_url = "http://0day.today"
        self.list_result = []
        self.regex_item = re.compile(r"(?msi)<div class='ExploitTableContent'.*?<div class='tips_value_big'>")
        self.regex_date = re.compile(r"(?msi)href='/date.*?>(\d{2})-(\d{2})-(\d{4})")
        self.regex_url = re.compile(r"(?msi)href='(/exploit.*?)'")
        self.regex_name = re.compile(r"(?msi)href='/exploit.*?'>([^<]*?)<")

    def run(self, ):
        try:
            url_search = self.url.format(self.key_word)
            req_worker = RequestWorker(url=url_search, data={'agree': 'Yes%2C+I+agree'},
                                       session_url=self.session_url)
            req_worker.start()
            self.list_req_workers.append(req_worker)
        except Exception as e:
            import traceback
            traceback.print_exc()
        self._get_results()

    def _parser(self, html):
        for item in self.regex_item.finditer(html):
            item_html = item.group(0)
            dict_result = {}
            dict_result['url'] = self.base_url + self.regex_url.search(item_html).group(1)
            match_date = self.regex_date.search(item_html)
            date = "{0}-{1}-{2}".format(match_date.group(3),
                                        match_date.group(2),
                                        match_date.group(1)
                                        )
            dict_result['date'] = date
            dict_result['name'] = self.regex_name.search(item_html).group(1)
            self.list_result.append(dict_result)


class Vulners(Scraper):
    def __init__(self, key_word):
        Scraper.__init__(self)
        self.name_site = "Vulners"
        self.name_class = Vulners.__name__
        self.key_word = key_word
        self.url_domain = "vulners.com"
        self.path = "/api/v3/search/lucene/"
        self.list_result = []
        self.regex_date = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

    def run(self, ):
        try:
            data = {}
            data['query'] = "{0} last year".format(self.key_word)
            req_worker = RequestWorkerHttpLib(self.url_domain, self.path, data)
            req_worker.start()
            self.list_req_workers.append(req_worker)
        except Exception as e:
            import traceback
            traceback.print_exc()
        self._get_results()

    def _parser(self, html):
        json_data = json.loads(html)
        for data in json_data['data']['search']:
            dict_result = {}
            dict_result['url'] = data["_source"]['href']
            dict_result['name'] = data["_source"]["title"]
            dict_result['date'] = self.regex_date.search(data["_source"]["published"]).group(0)
            self.list_result.append(dict_result)


class NationaVulnerabilityDB(Scraper):
    def __init__(self, key_word):
        Scraper.__init__(self)
        self.name_site = "NationaVulnerabilityDB"
        self.name_class = NationaVulnerabilityDB.__name__
        self.key_word = key_word
        self.url = "https://web.nvd.nist.gov/view/vuln/search-results?query={0}&search_type=all&cves=on&startIndex={1}"
        self.base_url = 'https://web.nvd.nist.gov/view/vuln/'
        self.page_max = 60
        self.list_result = []
        self.regex_item = re.compile(r'(?msi)<dt>.*?a href="detail.*?</dd>')
        self.regex_name = re.compile(r'(?msi)<dt>.*?Summary:.*?>([^<]*?)<')
        self.regex_date = re.compile(r'(?msi)<dt>.*?Summary:.*?>.*?Published:.*?>.*?(\d{1,2})\/(\d{1,2})\/(\d{4})')
        self.regex_url = re.compile(r'(?msi)<dt>.*?href="([^"]*?vulnId.*?)"')

    def run(self, ):
        for page in range(0,self.page_max+1,20):
            try:
                url_search = self.url.format(
                    self.key_word,
                    page
                )
                req_worker = RequestWorker(url_search)
                req_worker.start()
                self.list_req_workers.append(req_worker)
            except Exception as e:
                import traceback
                traceback.print_exc()
        self._get_results()

    def _parser(self, html):
        for item in self.regex_item.finditer(html):
            item_html = item.group(0)
            dict_results = {}
            dict_results['name'] = self.regex_name.search(item_html).group(1)
            match_date = self.regex_date.search(item_html)
            date = "{0}-{1}-{2}".format(match_date.group(3),
                                        match_date.group(1),
                                        match_date.group(2)
                                        )
            dict_results['date'] = date
            dict_results['url'] = self.base_url + self.regex_url.search(item_html).group(1)
            self.list_result.append(dict_results)

class WpvulndbB(Scraper):
    def __init__(self, key_word):
        Scraper.__init__(self)
        self.name_site = "Wpvulndb"
        self.name_class = NationaVulnerabilityDB.__name__
        self.key_word = key_word
        self.url = "https://wpvulndb.com/searches?page={1}&text={0}&utf8=%E2%9C%93&vuln_type="
        self.url_base = "https://wpvulndb.com"
        self.page_max = 2
        self.list_result = []
        self.regex_item = re.compile(r'(?msi)<tr>.*?<td>.*?<a.*?</tr>')
        self.regex_name = re.compile(r'(?msi)<a href="[^"]*?">\d+?<.*?href.*?>([^<]*?)<')
        self.regex_date = re.compile(r'(?msi)created-at">([^<]*?)<')
        self.regex_url = re.compile(r'(?msi)<a href="([^"]*?)">\d+?<')

    def run(self, ):
        for page in range(self.page_max+1):
            try:
                url_search = self.url.format(
                    self.key_word,
                    page
                )
                req_worker = RequestWorker(url_search)
                req_worker.start()
                self.list_req_workers.append(req_worker)
            except Exception as e:
                import traceback
                traceback.print_exc()
        self._get_results()

    def _parser(self, html):
        for item in self.regex_item.finditer(html):
            dict_results = {}
            item_html = item.group(0)
            url = self.url_base + self.regex_url.search(item_html).group(1)
            dict_results['url'] = url
            dict_results['name'] = self.regex_name.search(item_html).group(1)
            dict_results['date'] =  self.regex_date.search(item_html).group(1)
            self.list_result.append(dict_results)


