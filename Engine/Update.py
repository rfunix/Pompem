#-*- coding: UTF-8 -*-

import os
import time
from subprocess import PIPE
from subprocess import Popen as execute
import platform

class UpdateVersion():
    def __init__(self, gitRepository=None):
        self.gitRepository = "https://github.com/rfunix/Pompem.git"


    def update(self):
        if not os.path.dirname(os.path.abspath(__file__)):
            print("not a git repository. Please checkout the 'rfunix/Pompem' repository")
            print("from GitHub (e.g. git clone https://github.com/rfunix/Pompem.git")
        else:
            print ("updating Pompem to the latest development version from the GitHub repository")
            print ("[%s] [INFO] update in progress " % time.strftime("%X"))
            process = execute("git pull %s HEAD" % self.gitRepository, shell=True, stdout=PIPE, stderr=PIPE)
            self.companyingProcess(process)
            stdout, stderr = process.communicate()
            success = not process.returncode

            if success:
                print("Update was successful")
            else:
                print("Update unrealized")


            if not success:
                if "windows" in str(platform.system()).lower():
                    print("for Windows platform it's recommended ")
                    print("to use a GitHub for Windows client for updating ")
                    print("purposes (http://windows.github.com/) or just ")
                    print("download the latest snapshot from ")
                    print("https://github.com/rfunix/Pompem.git")
                else:
                    print("for Linux platform it's required ")
                    print("to install a standard 'git' package (e.g.: 'sudo apt-get install git')")

        return success

    def companyingProcess(self,process):

        while True:
            print(".")
            time.sleep(1)
            codeReturn = process.poll()
            if codeReturn is not None:
                if codeReturn == 0:
                    print(" done\n")
                elif codeReturn < 0:
                    print(" process terminated by signal %d\n" % codeReturn)
                elif codeReturn > 0:
                    print(" quit unexpectedly with return code %d\n" % codeReturn)
                break

