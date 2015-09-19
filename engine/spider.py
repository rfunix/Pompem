#!/usr/bin/python
# -*- coding:utf-8 -*-

from engine.functions import download_file
from datetime import date
import time
import sys
import re


class Spider(object):
    def __init__(self):
        self.amountDownload = 0
        self.urlsErrors = {}
        self.copyUrlErrors = {}
        
    def run(self,Results):
        regexNameDirectory = re.compile(r"http://(www\.)?(.*?)\.")
        for wordSearch, listResults in Results.items():
            if (not listResults[0]):
                print("\nWas no result found for {0}".format(wordSearch))
                return
            print ("+ Starting Downloads from {2} - {0} - {1}".format(date.today().strftime("%d/%m/%Y"),
                                                     time.strftime("%H:%M:%S"), wordSearch))  
            for listDictResults in listResults:
                for dictResults in listDictResults:
                    try:
                        matchName = regexNameDirectory.search(str(dictResults["Download"]))
                        if matchName:
                            fullDirectory = "./Exploits/{0}/{1}/".format(str(matchName.group(2)).replace(" ",""), wordSearch.replace(" ",""))
                            fullname = download_file(str(dictResults["Download"]),fullDirectory)
                            if fullname:
                                print ("+ {0} - {1} Full Path: {2} Download completed".format(date.today().strftime("%d/%m/%Y"),
                                                                         time.strftime("%H:%M:%S"),fullname))
                                self.amountDownload += 1
                    except Exception,ex:
                        print "ERROR: Url -> {0}".format(str(dictResults["Download"]))
                        if not dict(self.urlsErrors).has_key(wordSearch.replace(" ","")):
                            self.urlsErrors[wordSearch.replace(" ", "")] = []
                        self.urlsErrors[wordSearch.replace(" ","")].append(str(dictResults["Download"]))

        print ("+ Download finish {0} - {1} Total Number of Downloads: {2}".format(date.today().strftime("%d/%m/%Y"),
                                                                         time.strftime("%H:%M:%S"), self.amountDownload))
        while len(self.urlsErrors) > 0:
            if len(self.urlsErrors) > 0:
                self.copyUrlErrors = self.urlsErrors
                respost = str(raw_input("Some downloads have had problems and so have not been downloaded, you want to try again? [Y/N]"))
                if respost:
                    if respost.upper() == "Y" or respost.upper() == "N":
                        if respost.upper() == "Y":
                            self.urlsErrors = {}
                            self.amountDownload = 0
                            for wordSearch, listErrors in self.copyUrlErrors.items():
                                for url in listErrors:
                                    try:
                                        matchName = regexNameDirectory.search(str(url))
                                        if matchName:
                                            fullDirectory = "./Exploits/{0}/{1}/".format(str(matchName.group(2)).replace(" ",""), wordSearch.replace(" ",""))
                                            fullname = DownloadFile(str(url),fullDirectory)
                                            if fullname:
                                                print ("+ {0} - {1} Full Path: {2} Download completed".format(date.today().strftime("%d/%m/%Y"),
                                                                         time.strftime("%H:%M:%S"),fullname))
                                                self.amountDownload += 1
                                    except Exception,ex:
                                        print ("ERROR: Url -> {0}".format(url))
                                        if not dict(self.urlsErrors).has_key(wordSearch.replace(" ","")):
                                            self.urlsErrors[wordSearch.replace(" ", "")] = []
                                        self.urlsErrors[wordSearch.replace(" ","")].append(url)
                            print ("+ Download finish {0} - {1} Total Number of Downloads: {2}".format(date.today().strftime("%d/%m/%Y"),
                                                                         time.strftime("%H:%M:%S"), self.amountDownload))
                        else:
                            sys.exit(1)
                    else:
                        sys.exit(1)
                else:
                    sys.exit(1)