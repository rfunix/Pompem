# -*- coding: UTF-8 -*-

from Engine.Router import Router

def execute(listWords):
    print ("+ Searching Exploits ...")
    router = Router()
    router.words = listWords
    dictAllResults = router.searchInBots()
    for wordSearch, listResults in dictAllResults.items():
        countPrint = 0
        print ("+"+"-" * 150+"+")
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
        