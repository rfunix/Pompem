# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')
import optparse
from engine.update import UpdateVersion
from engine.exec_and_print import execute


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

    parser.add_option("-g","--get",
                  action="store_true", dest="get",
                  help="Download Exploits")


    parser.add_option("-h", "--help",
                      action="store_true", dest="help", help="-h")
    (options, args) = parser.parse_args()

    args_parameters = {}
    keywords = options.keywords
    fileText = options.fileText
    fileHtml = options.fileHtml
    update = options.update
    get = options.get
    
    help = options.help
    if help:
       print_help_message()
       return
    #keywords = "ssh"
    if (update):
        u = UpdateVersion()
        u.update() #Update from github
        return
    if (get):
        args_parameters["get"] = True
    if(keywords):
        keywordsformated = str(keywords).split(",")
        if fileText:
            args_parameters["fileText"] = fileText
        if fileHtml:
            args_parameters["fileHtml"] = fileHtml
        if keywordsformated:
            args_parameters["keywordsformated"] = keywordsformated
            args_parameters["keywords"] = keywords
        execute(**args_parameters)
    else:
        basic_info()
        return

def print_help_message():
     print """
Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt                           Write txt File
  --html                          Write html File
  --update                        upgrade to latest version
  -g, --get                       Download exploit files
              """

def basic_info():
     print """
            Pompem - Exploit Finder  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer and Ethical Hacker) - @rfunix\n
    Bruno Fraga (Security Researcher) - @brunofraga_net\n
              Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                               [--txt Write txt file                     ]
                               [--html Write html file                   ]
                               [-g/--get Download exploit files          ]
      \n              Get basic options and Help, use: -h\--help
              """

if __name__ == "__main__":
    main()
