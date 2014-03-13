# -*- coding: UTF-8 -*-

import sys
sys.path.insert(0, '..')
import optparse
from Engine.Update import UpdateVersion
from Engine.ExecAndPrint import execute


def main():
    parser = optparse.OptionParser(add_help_option=False)

    parser.add_option("-s", "--search", dest="keywords", type="string",
                                        help="text for search",)

    parser.add_option("--txt", dest="fileText", \
                      action="store_true", help="enter the file name",)

    parser.add_option("--html", dest="fileHtml", action="store_true", \
                      help="enter the file name",)

    parser.add_option("--update",
                  action="store_true", dest="update",
                  help="upgrade to latest version")

    parser.add_option("-h", "--help",
                      action="store_true", dest="help", help="-h")
    (options, args) = parser.parse_args()

    argsParameters = {}
    keywords = options.keywords
    fileText = options.fileText
    fileHtml = options.fileHtml
    update = options.update
    help = options.help
    if help:
       printHelpMessage()
       return
    #keywords = "ssh"
    if (update):
        u = UpdateVersion()
        u.update() #Update from github
        return
    if(keywords):
        if fileText:
            argsParameters["fileText"] = fileText
        if fileHtml:
            argsParameters["fileHtml"] = fileHtml
        keywordsformated = str(keywords).split(",")
        if keywordsformated:
            argsParameters["keywordsformated"] = keywordsformated
            argsParameters["keywords"] = keywords
            execute(**argsParameters)
    else:
        basicInfo()
        return

def printHelpMessage():
     print """
Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt                           Write txt File
  --html                          Write html File
  --update                        upgrade to latest version
              """

def basicInfo():
     print """
            Pompem - Exploit Finder  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer and Ethical Hacker) - @twitter\n
    Bruno Fraga (Security Researcher) - @brunofraga_net\n
              Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                               [--txt Write txt file  ]
                               [--html Write html file]
      \n              Get basic options and Help, use: -h\--help
              """

if __name__ == "__main__":
    main()
