import re
from collections import UserDict, defaultdict
from datetime import datetime
from urllib.parse import urljoin

from .request_worker import request_worker, request_worker_keep_session


class BaseScraper(UserDict):
    regex_item = None
    regex_url = None
    regex_name = None
    regex_date = None
    base_url = None
    max_page = None
    exploit_endpoint = None

    def __init__(self):
        super().__init__(self)
        self.data = defaultdict(list)

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    async def __call__(self, keyword):
        for page in range(self.max_page):
            url = urljoin(self.base_url, self.exploit_endpoint.format(page, keyword))
            html_page = await request_worker(url)
            self.data[keyword] += list(self.parser(html_page))

    def parser(self, html):
        for item in self.regex_item.finditer(html):
            yield self.build_exploit(item.group(0))

    def build_exploit(self, regex_item):
        return {
            "url": self.get_exploit_url(regex_item),
            "date": self.get_exploit_date(regex_item),
            "name": self.get_exploit_name(regex_item),
        }

    def get_exploit_url(self, regex_item):
        return "{0}{1}".format(self.base_url, self.regex_url.search(regex_item).group(1))

    def get_exploit_date(self, regex_item):
        return self.regex_date.search(regex_item).group(1)

    def get_exploit_name(self, regex_item):
        return self.regex_name.search(regex_item).group(1)


class PacketStorm(BaseScraper):
    regex_item = re.compile(r'(?ms)(<dl id="[^"]*?".*?<\/dl>)')
    regex_url = re.compile(r'href="(/files/\d+?\/[^"]*?)"')
    regex_date = re.compile(r'href="/files/date/(\d{4}-\d{2}-\d{2})')
    regex_name = re.compile(r'href="/files/\d+?\/[^"]*?".*?title.*?>([^<]*?)<')
    base_url = "https://packetstormsecurity.com"
    exploit_endpoint = "search/files/page{}/?q={}"
    max_page = 1


class CXSecurity(BaseScraper):
    regex_item = re.compile(r'(?msi)<tr>.*?<td width="17".*?<td width="550".*?</tr>')
    regex_url = re.compile(r'(?msi)<td.*?<h6><a href="([^"]*?)"')
    regex_date = re.compile(r'(?msi)<td width="80".*?default">(\d{2})\.(\d{2})\.(\d{4})')
    regex_name = re.compile(r'(?msi)title="([^"]*?)"')
    base_url = "https://cxsecurity.com"
    exploit_endpoint = "search/wlb/DESC/AND/{}.1999.1.1/{}/30/{}/"
    max_page = 1

    async def __call__(self, keyword):
        formated_date = "{dt.year}.{dt.month}.{dt.day}".format(dt=datetime.utcnow())

        for page in range(self.max_page):
            url = urljoin(self.base_url, self.exploit_endpoint.format(formated_date, page, keyword))
            html_page = await request_worker(url)
            self.data[keyword] += list(self.parser(html_page))

    def get_exploit_date(self, regex_item):
        return "{0}-{1}-{2}".format(
            self.regex_date.search(regex_item).group(1),
            self.regex_date.search(regex_item).group(2),
            self.regex_date.search(regex_item).group(3),
        )


class ZeroDay(BaseScraper):
    regex_item = re.compile(r"(?msi)<div class='ExploitTableContent'.*?<div class='tips_value_big'>")
    regex_date = re.compile(r"(?msi)href='/date.*?>(\d{2})-(\d{2})-(\d{4})")
    regex_url = re.compile(r"(?msi)href='(/exploit.*?)'")
    regex_name = re.compile(r"(?msi)href='/exploit.*?'>([^<]*?)<")
    base_url = "http://www-.0day.today"
    exploit_endpoint = "search?search_request={}"
    max_page = 1

    async def __call__(self, keyword):
        for _ in range(self.max_page):
            url = urljoin(self.base_url, self.exploit_endpoint.format(keyword))
            html_page = await request_worker_keep_session(
                url=url, session_url=self.base_url, data={"agree": "Yes%2C+I+agree"}
            )
            self.data[keyword] += list(self.parser(html_page))

    def get_exploit_date(self, regex_item):
        return "{0}-{1}-{2}".format(
            self.regex_date.search(regex_item).group(1),
            self.regex_date.search(regex_item).group(2),
            self.regex_date.search(regex_item).group(3),
        )
