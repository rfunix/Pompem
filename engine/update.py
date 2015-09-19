#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os
import time
from subprocess import PIPE
from subprocess import Popen as execute
import platform

class UpdateVersion():
    def __init__(self, git_repository="https://github.com/rfunix/Pompem.git"):
        self.git_repository = git_repository

    def update(self):
        if not os.path.dirname(os.path.abspath(__file__)):
            print ("not a git repository. Please checkout " +
                "the 'rfunix/Pompem' repository")
            print("from GitHub (e.g. git clone " +
                "https://github.com/rfunix/Pompem.git Pompem-dev")
        else:
            print ("updating Pompem to the latest development version" +
                " from the GitHub repository")
            print ("[{0}] [INFO] update in progress ".format(
                                                        time.strftime("%X")))
            process = execute("git pull {0} HEAD".format(self.git_repository), 
                                shell=True, stdout=PIPE, stderr=PIPE)
            self.companying_process(process)
            stdout, stderr = process.communicate()
            success = not process.returncode

            if success:
                print("Update was successful")
            else:
                print("Update unrealized")


            if not success:
                if "windows" in str(platform.system()).lower():
                    print ("for Windows platform it's recommended ")
                    print ("to use a GitHub for Windows client for updating ")
                    print ("purposes (http://windows.github.com/) or just ")
                    print ("download the latest snapshot from ")
                    print ("https://github.com/rfunix/Pompem.git")
                else:
                    print ("for Linux platform it's required ")
                    print ("to install a standard 'git' package" + 
                            "(e.g.: 'sudo apt-get install git')")

        return success

    def companying_process(self, process):
        while True:
            print(".")
            time.sleep(1)
            code_return = process.poll()
            if code_return is not None:
                if code_return == 0:
                    print (" done\n")
                elif code_return < 0:
                    print (" process terminated by signal {0}\n".format(codeReturn))
                elif code_return > 0:
                    print(" quit unexpectedly with return code {0}\n".format(codeReturn))
                break

