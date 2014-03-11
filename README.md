Pompem - Exploit Finder
==

Pompem is an open source tool, which is designed to automate the search for exploits in major databases.
Developed in Python, has a system of advanced search, thus facilitating the work of pentesters and ethical hackers.
In its current version, performs searches in databases: Exploit-db, 1337day, Packetstorm Security...

Screenshots
----


Installation
----

You can download the latest tarball by clicking [here](https://github.com/rfunix/Pompem/tarball/master) or latest zipball by clicking  [here](https://github.com/rfunix/Pompem/zipball/master).

Preferably, you can download sqlmap by cloning the [Git](https://github.com/rfunix/Pompem) repository:

    git clone https://github.com/rfunix/Pompem.git Pompem-dev

Pompem works out of the box with [Python](http://www.python.org/download/) version '''2.6.x''' and '''2.7.x''' on any platform.


Usage
----

To get the list of basic options and information about the project:

    python pompem.py -h
    
Examples of use:

    python pompem.py -s Wordpress --txt output.txt
    python pompem.py -s Joomla --html output.html
    python pompem.py -s ssh,ftp,telnet
    python pompem.py --update
