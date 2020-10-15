MAX_PRINT_PER_SITE = 50


def get_help_message():
    return """
Options:
  -h, --help                      show this help message and exit
  -s, --search <keyword,keyword,keyword>  text for search
  --txt                           Write txt File
  --html                          Write html File
              """


def get_basic_info():
    return """

           __________
           \______   \____   _____ ______   ____   _____
            |     ___/  _ \ /      \____ \_/ __ \ /     \
            |    |  (  <_> )  Y Y  \  |_> >  ___/|  Y Y  \
            |____|   \____/|__|_|  /   __/ \___  >__|_|  /
                                 \/|__|        \/      \/


    Rafael Francischini (Programmer and Ethical Hacker) - @rfunix
    Bruno Fraga (Security Researcher) - @brunofraga_net

    Usage: pompem.py [-s/--search <keyword,keyword,keyword,...>]
                     [--txt Write txt file                     ]
                     [--html Write html file                   ]
                  Get basic options and Help, use: -h\--help
              """


def show_results(keyword, exploits):
    print("+Results {0}".format(keyword))
    print("+" + "-" * 150 + "+")
    print(
        "+Date            Description                                     Url                                    "
    )
    print("+" + "-" * 150 + "+")

    count_exploits = 0
    for exploit in exploits:
        if count_exploits > MAX_PRINT_PER_SITE:
            break
        count_exploits += 1
        print(
            "+ {0} | {1} | {2} ".format(
                exploit["date"], str(exploit["name"])[0:50], exploit["url"]
            )
        )
        print("+" + "-" * 150 + "+")
