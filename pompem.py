# -*- coding: UTF-8 -*-

import sys
sys.path.insert(0, '..')
import optparse
from Engine.Update import UpdateVersion
from Engine.ExecAndPrint import execute


def main():
    parser = optparse.OptionParser("%prog " + \
                                   "-s --search <word,word,word...> --txt <Save Text File> --html <Save Html File>")

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
        execute(listWords)
    else:
        print(parser.get_usage())


if __name__ == "__main__":
    main()
