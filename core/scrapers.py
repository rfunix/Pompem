import re
from datetime import datetime
from collections import defaultdict
from collections import UserDict
from core.parser_config import configs
from core.request_worker import request_worker, request_worker_keep_session


class BaseScraper(UserDict):
    def __init__(self):
        UserDict.__init__(self)
        self.data = defaultdict(list)
        self.configs = configs["scrapers"][type(self).__name__.lower()]
        self.regex_item = None
        self.regex_url = None
        self.regex_name = None
        self.regex_date = None

    def __getitem__(self, item):
        return self.data[item]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    async def __call__(self, *args, **kwargs):
        keyword = kwargs.get("keyword", None)
        for page in (1, range(self.configs["max_page"])):
            self.data[keyword] += [_ async for _ in self.parser(
                await request_worker(self.configs["url"].format(page, keyword)))]

    async def parser(self, html):
        for item in self.regex_item.finditer(html):
            if item:
                exploit = self.build_exploit(item.group(0))
                yield exploit

    def build_exploit(self, regex_item):
        return {'url': self.get_exploit_url(regex_item), 'date': self.get_exploit_date(regex_item),
                'name': self.get_exploit_name(regex_item)}

    def get_exploit_url(self, regex_item):
        return "{0}{1}".format(
            self.configs["base_url"],
            self.regex_url.search(regex_item).group(1)
        )

    def get_exploit_date(self, regex_item):
        return self.regex_date.search(regex_item).group(1)

    def get_exploit_name(self, regex_item):
        return self.regex_name.search(regex_item).group(1)


class PacketStorm(BaseScraper):
    def __init__(self):
        BaseScraper.__init__(self)
        self.regex_item = re.compile(r'(?ms)(<dl id="[^"]*?".*?<\/dl>)')
        self.regex_url = re.compile(r'href="(/files/\d+?\/[^"]*?)"')
        self.regex_date = re.compile(r'href="/files/date/(\d{4}-\d{2}-\d{2})')
        self.regex_name = re.compile(r'href="/files/\d+?\/[^"]*?".*?title.*?>([^<]*?)<')


class CXSecurity(BaseScraper):
    def __init__(self):
        BaseScraper.__init__(self)
        self.regex_item = re.compile(r'(?msi)<tr>.*?<td width="17".*?<td width="550".*?</tr>')
        self.regex_url = re.compile(r'(?msi)<td.*?<h6><a href="([^"]*?)"')
        self.regex_date = re.compile(r'(?msi)<td width="80".*?default">(\d{2})\.(\d{2})\.(\d{4})')
        self.regex_name = re.compile(r'(?msi)title="([^"]*?)"')

    async def __call__(self, *args, **kwargs):
        now_date = '{dt.year}.{dt.month}.{dt.day}'.format(
            dt=datetime.now()
        )
        keyword = kwargs.get("keyword", None)
        for page in range(0, self.configs["max_page"]):
            self.data[keyword] += [_ async for _ in self.parser(
                await request_worker(self.configs["url"].format(now_date, page, self.configs['max_page'],
                                                                keyword)))]
    def get_exploit_date(self, regex_item):
        return "{0}-{1}-{2}".format(self.regex_date.search(regex_item).group(1),
                                    self.regex_date.search(regex_item).group(2),
                                    self.regex_date.search(regex_item).group(3))

class ZeroDay(BaseScraper):
    def __init__(self):
        BaseScraper.__init__(self)
        self.regex_item = re.compile(r"(?msi)<div class='ExploitTableContent'.*?<div class='tips_value_big'>")
        self.regex_date = re.compile(r"(?msi)href='/date.*?>(\d{2})-(\d{2})-(\d{4})")
        self.regex_url = re.compile(r"(?msi)href='(/exploit.*?)'")
        self.regex_name = re.compile(r"(?msi)href='/exploit.*?'>([^<]*?)<")

    async def __call__(self, *args, **kwargs):
        keyword = kwargs.get("keyword", None)
        for _ in (1, range(self.configs["max_page"])):
            self.data[keyword] += [_ async for _ in self.parser(
                await request_worker_keep_session(url=self.configs["url"].format(keyword),
                                                  session_url=self.configs["base_url"],
                                                  data={'agree': 'Yes%2C+I+agree'})
            )]

    def get_exploit_date(self, regex_item):
        return "{0}-{1}-{2}".format(self.regex_date.search(regex_item).group(1),
                                    self.regex_date.search(regex_item).group(2),
                                    self.regex_date.search(regex_item).group(3))
