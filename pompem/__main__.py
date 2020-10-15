import asyncio
import optparse

from .exploit_finder import ExploitFinder
from .messages import get_help_message, get_basic_info


def main():
    parser = optparse.OptionParser(add_help_option=False)

    parser.add_option("-s", "--search", dest="keywords", type="string", help="text for search")

    parser.add_option("--txt", dest="txt_out", action="store_true", help="Generate txt output file")

    parser.add_option("--html", dest="html_out", action="store_true", help="Generate html output file")

    parser.add_option("--update", action="store_true", dest="update", help="upgrade to latest version")

    parser.add_option("-g", "--get", action="store_true", dest="get_exploit", help="Download Exploits")

    parser.add_option("-h", "--help", action="store_true", dest="help", help="-h")

    args = parser.parse_args()[0]

    if not args.help and args.keywords:
        exploit_finder = ExploitFinder(args)
        return asyncio.run(exploit_finder.run())
    else:
        print(get_help_message())

    print(get_basic_info())


if __name__ == "__main__":
    main()
