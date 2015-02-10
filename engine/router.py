# -*- coding: utf-8 -*-
import sys
from bots.exploit_db import ExploitDB
from bots.packet_storm import PacketStorm
from bots.day import BotDay
from bots.security_vulns import SecurityVulns
from threading import Thread

sys.path.insert(0, '..')

class Router(object):
    def __init__(self, words=None, dictAllResults={}, listWordResults=[]):
        self.dictAllResults = dictAllResults
        self.listWordResults =listWordResults
        self.words = words

    def searchInBots(self):
        if self.words:
            try:
                for word in self.words:
                    self.listWordResults = []
                    if(word):
                        th1 = Thread(target=self.addBotExploitDB, args=(word,))
                        th1.start()
                        th1.join()
                        th2 = Thread(target=self.addBotPacketStorm, args=(word,))
                        th2.start()
                        th2.join()
                        th3 = Thread(target=self.addBotDay, args=(word,))
                        th3.start()
                        th3.join()
                        th4 = Thread(target=self.addSecurityVulns, args=(word,))
                        th4.start()
                        th4.join()
                        self.dictAllResults[word] = self.listWordResults
                return self.dictAllResults
            except Exception, ex:
                pass


    def addBotPacketStorm(self, word):
        packetStorm = PacketStorm()
        packetStorm.filter_description = word
        self.listWordResults.append(packetStorm.bot_search())

    def addBotExploitDB(self, word):
        exploitDB = ExploitDB()
        exploitDB.filter_description = str(word).strip("\n")
        self.listWordResults.append(exploitDB.bot_search())

    def addBotDay(self, word):
        day = BotDay()
        day.filter_description = str(word).strip("\n")
        self.listWordResults.append(day.bot_search())

    def addSecurityVulns(self, word):
        sec = SecurityVulns()
        sec.filter_description = str(word).strip("\n")
        self.listWordResults.append(sec.bot_search())
