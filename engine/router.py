#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

from bots.security_vulns import SecurityVulns
from bots.packet_storm import PacketStorm
from bots.exploit_db import ExploitDB
from threading import Thread
from bots.day import BotDay


class Router(object):
    def __init__(self, words=None, dic_all_results={}, list_word_results=[]):
        self.dic_all_results = dic_all_results
        self.list_word_results = list_word_results
        self.words = words

    def search_in_bots(self):
        if self.words:
            try:
                for word in self.words:
                    self.list_word_results = []
                    if(word):
                        th1 = Thread(
                            target=self.add_bot_exploit_db, 
                            args=(word,))
                        th1.start()
                        th1.join()
                        th2 = Thread(
                            target=self.add_bot_packet_storm, 
                            args=(word,))
                        th2.start()
                        th2.join()
                        #th3 = Thread(
                        #    target=self.add_bot_day, 
                        #    args=(word,))
                        #th3.start()
                        #th3.join()
                        th4 = Thread(
                            target=self.add_security_vulns, 
                            args=(word,))
                        th4.start()
                        th4.join()
                        self.dic_all_results[word] = self.list_word_results
                return self.dic_all_results
            except Exception, ex:
                pass


    def add_bot_packet_storm(self, word):
        packetStorm = PacketStorm()
        packetStorm.filter_description = word
        self.list_word_results.append(packetStorm.bot_search())

    def add_bot_exploit_db(self, word):
        exploitDB = ExploitDB()
        exploitDB.filter_description = str(word).strip("\n")
        self.list_word_results.append(exploitDB.bot_search())

    def add_bot_day(self, word):
        day = BotDay()
        day.filter_description = str(word).strip("\n")
        self.list_word_results.append(day.bot_search())

    def add_security_vulns(self, word):
        sec = SecurityVulns()
        sec.filter_description = str(word).strip("\n")
        self.list_word_results.append(sec.bot_search())
