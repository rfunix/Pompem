# -*- coding: UTF-8 -*-
import sys
from Bots.Exploitdb import ExploitDB
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
                        th = Thread(target=self.addBotExploitDB, args=(word,))
                        th.start()
                        th.join()
                        #create other bots
                        self.dictAllResults[word] = self.listWordResults
                return self.dictAllResults
            except Exception, ex:
                pass


    def addBotExploitDB(self, word):
        exploitDB = ExploitDB()
        exploitDB.filter_description = str(word).strip("\n")
        self.listWordResults.append(exploitDB.botSearch())
