#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import optparse
from core.exploit_finder import ExploitFinder
from common.print_messages import HELP_MESSAGE, BASIC_INFO_MESSAGE


def main():
    parser = optparse.OptionParser(add_help_option=False)

    parser.add_option("-s", "--search", dest="keywords", type="string",
                      help="text for search", )

    parser.add_option("--txt", dest="txt_out",
                      action="store_true", help="Generate txt output file", )

    parser.add_option("--html", dest="html_out", action="store_true",
                      help="Generate html output file", )

    parser.add_option("--update",
                      action="store_true", dest="update",
                      help="upgrade to latest version")

    parser.add_option("-g", "--get",
                      action="store_true", dest="get_exploit",
                      help="Download Exploits")

    parser.add_option("-h", "--help",
                      action="store_true", dest="help", help="-h")

    args = parser.parse_args()
    parameters = args[0]

    if not parameters.keywords:
        if parameters.help:
            print (HELP_MESSAGE)
            exit(0)
        else:
            print (BASIC_INFO_MESSAGE)
            exit(0)

    exploit_finder = ExploitFinder(parameters)
    exploit_finder.run()


if __name__ == "__main__":
    main()
