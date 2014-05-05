# Pompem - Exploit Finder

Pompem is an open source tool, which is designed to automate the search for exploits in major databases.
Developed in Python, has a system of advanced search, thus facilitating the work of pentesters and ethical hackers.
In its current version, performs searches in databases: Exploit-db, 1337day, Packetstorm Security...

## Screenshots
![](http://i61.tinypic.com/34hvqm0.png)


## Installation


You can download the latest tarball by clicking [here](https://github.com/rfunix/Pompem/tarball/master) or latest zipball by clicking  [here](https://github.com/rfunix/Pompem/zipball/master).

Preferably, you can download pompem by cloning the [Git](https://github.com/rfunix/Pompem) repository:

```
git clone https://github.com/rfunix/Pompem.git Pompem-dev
```

Pompem works out of the box with [Python](http://www.python.org/download/) version '''2.6.x''' and '''2.7.x''' on any platform.

Pompem lib uses the following setup:

* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
* [Requests](http://docs.python-requests.org/en/latest/)

If you have not realized the Download or use virtualenv:

1. Create virtual env with ```virtualenv .env```
2. Activate virtualenv with ```source .env/bin/activate```
3. Install dependêncies with ```pip install -r requeriments.txt```

> If you use pip and have not vitualenv use 'sudo pip install virtualenv' or see [virtualenv website](http://www.virtualenv.org/en/latest/).


## Usage

To get the list of basic options and information about the project:

```bash
python pompem.py -h
```

Examples of use:

    python pompem.py -s Wordpress
    python pompem.py -s Joomla --html
    python pompem.py -s "Internet Explorer,joomla,wordpress" --html
    python pompem.py -s FortiGate --txt
    python pompem.py -s ssh,ftp,mysql
    python pompem.py --update
    

## License

Pompem is program is free software; you may redistribute and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; Version 2 with the clarifications and exceptions described in the license file. This guarantees your right to use, modify, and redistribute this software under certain conditions. If you wish to embed Pompem technology into proprietary software, we sell alternative licenses (contact officer@brunofraga.net). 

Pompem is free software, keeping the picture can USE AND ABUSE 
