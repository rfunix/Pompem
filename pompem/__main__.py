import asyncio
import optparse

from .exploit_finder import ExploitFinder

BASIC_INFO_MESSAGE = """
           __________
           \______   \____   _____ ______   ____   _____
            |     ___/  _ \ /      \\____ \_/ __ \ /      \\
            |    |  (  <_> )  Y Y  \  |_> >  ___/|  Y Y  \\
            |____|   \____/|__|_|  /   __/ \___  >__|_|  /
                                 \/|__|        \/      \/

    Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                     [--txt Write txt file                     ]
                     [--html Write html file                   ]
                  Get basic options and help, use: -h\--help
              """


def main():
    parser = optparse.OptionParser(add_help_option=False)

    parser.add_option("-s", "--search", dest="keywords", type="string", help="text for search")

    parser.add_option("--txt", dest="txt_out", action="store_true", help="Generate txt output file")

    parser.add_option("--html", dest="html_out", action="store_true", help="Generate html output file")

    parser.add_option("-h", "--help", action="store_true", dest="help", help="-h")

    (options, _) = parser.parse_args()

    if options.keywords:
        exploit_finder = ExploitFinder(options)
        return asyncio.run(exploit_finder.run())

    print(BASIC_INFO_MESSAGE)


if __name__ == "__main__":
    main()
