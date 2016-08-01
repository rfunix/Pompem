#!/usr/bin/python
# -*- coding: utf-8 -*-

HELP_MESSAGE =  """
Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt                           Write txt File
  --html                          Write html File
  --update                        upgrade to latest version
  -g, --get                       Download exploit files
              """

BASIC_INFO_MESSAGE = """
            Pompem - Exploit Finder  |  Developed by Relax Lab
              \n    Rafael Francischini (Programmer and Ethical Hacker) - @rfunix\n
    Bruno Fraga (Security Researcher) - @brunofraga_net\n
              Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                               [--txt Write txt file                     ]
                               [--html Write html file                   ]
      \n              Get basic options and Help, use: -h\--help
              """

GENERATE_TXT_FILE = """
+ Generate txt output file -> out.txt
"""


MAX_PRINT_PER_SITE = 30

def show_results(key_word, list_results):
    print ("+Results {0}".format(key_word))
    print ("+" + "-" * 200 + "+")
    print (
        "+Date            Description                                     Url                                    ")
    print ("+" + "-" * 200 + "+")

    for dict_result in list_results:
        count_print = 0
        for result in dict_result.itervalues():
            for exploit_data in result:
                if (count_print > MAX_PRINT_PER_SITE):
                    break
                count_print += 1
                print("+ {0} | {1} | {2} ".format(exploit_data["date"],
                                                        str(exploit_data["name"])[0:50],
                                                        exploit_data["url"]))
                print ("+" + "-" * 200 + "+")
