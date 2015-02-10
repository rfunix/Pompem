#-*- coding:utf-8 -*-

from engine.functions import DownloadPage
from model.result import Result
import abc
import re


class Base(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filter_description=None, results=[]):
        self.filter_description = filter_description
        self.results = results
        self.object_download = DownloadPage()

    @abc.abstractmethod
    def bot_search(self):
        pass

    @abc.abstractmethod
    def extract_data(self, html):
        pass
