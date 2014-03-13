# -*- coding: UTF-8 -*-

from Engine.Router import Router
from Engine.Functions import WriteHtml,WriteTxt
import webbrowser

def execute(**kwargs):
    print ("+ Searching Exploits for {0}...".format(kwargs["keywords"]))
    router = Router()
    router.words = kwargs["keywordsformated"]
    dictAllResults = router.searchInBots()

    if (dict(kwargs).has_key("fileText")):
        try:
            WriteTxt(dictAllResults)
            print("Your results will be saved in txt - out.txt")
            if(not dict(kwargs).has_key("fileHtml")):
                return
        except Exception, ex:
            print "ERROR -> {0}".format(ex.message)

    if (dict(kwargs).has_key("fileHtml")):
        try:
            WriteHtml(dictAllResults)
            print("Your results will be saved in html - out.html")
            new = 2
            url = "out.html"
            webbrowser.open(url,new=new)
            return
        except Exception, ex:
            print "ERROR -> {0}".format(ex.message)

    for wordSearch, listResults in dictAllResults.items():
        if (not listResults[0]):
            print("\nWas no result found for {0}".format(wordSearch))
            continue

        countPrint = 0
        print ("+Results {0}".format(wordSearch))
        print ("+"+"-" * 150+"+")
        print ("+Date            Description                                     Download                                       Author")
        print ("+"+"-" * 150+"+")

        for listDictResults in listResults:
            countPrint = 0
            for dictResults in listDictResults:
                if (countPrint > 15):
                    break
                countPrint +=1
                print("+ {0} | {1} | {2} | {3} ".format(dictResults["Date"],
                        str(dictResults["Description"])[0:40],
                        dictResults["Download"], str(dictResults["Author"])[0:20]))
                print ("+"+"-" * 150+"+")


