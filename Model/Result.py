# -*- coding: UTF-8 -*-
import sys
sys.path.insert(0, '..')

class Result:
    def __init__(self, date=None, description=None, author=None):
        self.date = date
        self.description = description
        self.author = author
