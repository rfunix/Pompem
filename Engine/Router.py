# -*- coding: UTF-8 -*-
import sys
from Bots.Exploitdb import ExploitDB
from Bots.PacketStorm import PacketStorm
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
                        self.dictAllResults[word] = self.listWordResults
                return self.dictAllResults
            except Exception, ex:
                pass


    def addBotPacketStorm(self, word):
        packetStorm = PacketStorm()
        packetStorm.filter_description = word
        self.listWordResults.append(packetStorm.botSearch())

    def addBotExploitDB(self, word):
        exploitDB = ExploitDB()
        exploitDB.filter_description = str(word).strip("\n")
        self.listWordResults.append(exploitDB.botSearch())
