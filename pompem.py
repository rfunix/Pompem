# -*- coding: UTF-8 -*-

import sys
sys.path.insert(0, '..')
import optparse
from Engine.Router import Router
from Engine.Update import UpdateVersion

def main():
    parser = optparse.OptionParser("%prog " + \
                                   "-s/--search <word,word,word...> --txt <Save Text File> --html <Save Html File>")

    parser.add_option("-s", "--search", dest="listWords", type="string",
                                        help="enter text to search",)

    parser.add_option("--txt", dest="fileText", type="string", \
                      help="enter the file name",)

    parser.add_option("--html", dest="fileHtml", type="string", \
                      help="enter the file name",)

    parser.add_option("--update",
                  action="store_true", dest="update",
                  help="upgrade to latest version")

    (options, args) = parser.parse_args()

    listWords = options.listWords
    fileTextName = options.fileText
    fileHtmlName = options.fileHtml
    update = options.update
    #listWords = "ssh"
    if (update):
        u = UpdateVersion()
        u.update() #Update from github
        return
    if(listWords):
        listWords = str(listWords).split(",")
    if listWords:
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
                    print("+ {0} | {1} | {2} | {3} ".format(dictResults["Date"], str(dictResults["Description"])[0:40], dictResults["Download"], str(dictResults["Author"])[0:20]))
    else:
        print(parser.get_usage())


if __name__ == "__main__":
    main()
