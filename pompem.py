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

    parser.add_option("--txt", dest="fileText", type="string", \
                      help="enter the file name",)

    parser.add_option("--html", dest="fileHtml", type="string", \
                      help="enter the file name",)

    parser.add_option("--update",
                  action="store_true", dest="update",
                  help="upgrade to latest version")

    parser.add_option("-h", "--help",
                      action="store_true", dest="help", help="-h")
    (options, args) = parser.parse_args()

    keywords = options.keywords
    fileTextName = options.fileText
    fileHtmlName = options.fileHtml
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
        keywordsformated = str(keywords).split(",")
        if keywordsformated:
            execute(keywordsformated, keywords)
    else:
        basicInfo()
        return

def printHelpMessage():
     print """
Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt=FILETEXT                  enter the file name
  --html=FILEHTML                 enter the file name
  --update                        upgrade to latest version
              """

def basicInfo():
     print """
            Pompem - Exploit Finder  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer and Ethical Hacker) - @twitter\n
    Bruno Fraga (Security Researcher) - @brunofraga_net\n
              Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                               [--txt <Save Text File>]
                               [--html <Save HTML File>]
      \n           More and Help, use: -h\--help
              """

if __name__ == "__main__":
    main()
