# -*- coding: UTF-8 -*-

from Engine.Router import Router
import sys

def execute(**kwargs):
    print ("+ Searching Exploits for {0}...".format(kwargs["keywords"]))
    router = Router()
    router.words = kwargs["keywordsformated"]
    dictAllResults = router.searchInBots()
    if (dict(kwargs).has_key("fileTextName")):
        try:
            createTxt(dictAllResults, kwargs["fileTextName"])
            print("Your results will be saved in txt - {0}".format(kwargs["fileTextName"]))
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


def createTxt(dictAllResults, filename):
    f = open(filename, "w")
    for wordSearch, listResults in dictAllResults.items():
        if (not listResults[0]):
            continue
        f.write("+"+"-" * 150+"+\n")
        f.write("+Results {0}\n".format(wordSearch))
        f.write("+"+"-" * 150+"+\n")
        f.write("+Date            Description                                     Download                                       Author\n")
        f.write("+"+"-" * 150+"+\n")
        for listDictResults in listResults:
            for dictResults in listDictResults:
                f.write("+ {0} | {1} | {2} | {3} \n".format(dictResults["Date"],
                        str(dictResults["Description"]),
                        dictResults["Download"], str(dictResults["Author"])))
                f.write("+"+"-" * 150+"+\n")
    f.close()
