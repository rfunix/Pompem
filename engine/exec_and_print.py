# coding: utf-8 

from engine.router import Router
from engine.functions import write_html, write_txt
from engine.spider import Spider
import webbrowser

def execute(**kwargs):
    
    print ("+ Searching Exploits for {0}...".format(kwargs["keywords"]))
    router = Router()
    
    if (dict(kwargs).has_key("spider")):
        router.words = "Exploit"
    else:
        router.words = kwargs["keywordsformated"]
    
    dict_all_results = router.search_in_bots()

    if (dict(kwargs).has_key("get")):
        try:
            s = Spider()
            s.run(dict_all_results)
        except Exception, ex:
            print "ERROR -> {0}".format(ex.message)

    if (dict(kwargs).has_key("fileText")):
        try:
            write_txt(dict_all_results)
            print("Your results will be saved in txt - out.txt")
            if(not dict(kwargs).has_key("fileHtml")):
                return
        except Exception, ex:
            print "ERROR -> {0}".format(ex.message)

    if (dict(kwargs).has_key("fileHtml")):
        try:
            write_html(dict_all_results)
            print("Your results will be saved in html - out.html")
            new = 2
            url = "out.html"
            webbrowser.open(url,new=new)
            return
        except Exception, ex:
            print "ERROR -> {0}".format(ex.message)

    if (not dict(kwargs).has_key("get")):
        for word_search, listResults in dict_all_results.items():
            if (not listResults[0]):
                print("\nWas no result found for {0}".format(word_search))
                continue

            countPrint = 0
            print ("+Results {0}".format(word_search))
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


