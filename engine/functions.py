# -*- coding: utf-8 -*-

import requests
import sys
import os
from BeautifulSoup import BeautifulStoneSoup
sys.path.insert(0, '..')

class DownloadPage(object):
    def __init__(self, url=None):
        self.url = url
        self.__headers = {
            'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'
        }

    def getDownloadPage(self, host=None, parametros=None):
        try:
            r = requests.get(host, params=parametros, headers=self.__headers)

            decodedstring = BeautifulStoneSoup(
                r.text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
            return str(decodedstring)
        except Exception, e:
            print (e.message)
            return None

    def postDownloadPageDay(self, host=None, postData={}):
        s = requests.session()
        s.post(host, headers=self.__headers, data={"agree":"OK"})
        r = s.post(host, headers=self.__headers, data=postData)
        
        decodedstring = BeautifulStoneSoup(
            r.text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
        return decodedstring


def WriteTxt(dictAllResults):
    for wordSearch, listResults in dictAllResults.items():
        if (not listResults[0]):
            continue
        with open("out.txt", "w") as f:
            f.write("+"+"-" * 150+"+\n")
            f.write("+Results {0}\n".format(wordSearch))
            f.write("+"+"-" * 150+"+\n")
            f.write("+Date            Description                                     Download                                       Author\n")
            f.write("+"+"-" * 150+"+\n")
            for listDictResults in listResults:
                for dictResults in listDictResults:
                    f.write("+ {0} | {1} | {2} | {3} \n".format(
                        dictResults["Date"],
                        str(dictResults["Description"]),
                        dictResults["Download"], str(dictResults["Author"])
                        )
                    )
                    f.write("+"+"-" * 150+"+\n")

def DownloadFile(url, directory):
    local_filename = url.split('/')[-1]
    full_file_name = "{0}{1}".format(directory, local_filename)
    r = requests.get(url, stream=True)
    if not os.path.exists(os.path.dirname(full_file_name)):
        os.makedirs(os.path.dirname(full_file_name))
    with open(full_file_name, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
                f.flush()
    return full_file_name


def WriteHtml(dictAllResults):
    with open(r"out.html", "w") as f:
        f.write(r'''
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title> Pompem - Exploit Finder </title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        background-color: #000000;
      }

      .colorFonts{
          color: lime;
      }
    </style>
    <link href="bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
  </head>
  <body>
    <div class="container">
    <div class="row-fluid">
        <div class="span12">
            <center>
                <h1 class="colorFonts">Pompem - Finder Exploit Tool</h1>
                <h2 class="colorFonts">  Relax Lab  </h2>
            </center>
        </div>
    </div>
      <br>
      <h3 class="colorFonts"> Results for search: </h3>
      <br>
      <br>
        ''')

        for wordSearch, listResults in dictAllResults.items():
            if (not listResults[0]):
                continue

            f.write(r'''
                <center>
                    <h3 class="colorFonts"> {0} </h3>
                </center>
                <br>
                <br>
                <table class="table colorFonts">
                    <thead>
                        <tr>
                            <td></td>
                            <th>Date </th>
                            <th>Description</th>
                            <th>Download</th>
                            <th>Author</th>
                        </tr>
                    </thead>
              <tbody>

            '''.format(wordSearch))

            for listDictResults in listResults:
                for dictResults in listDictResults:
                    f.write(r'''
                    <tr>
                        <td></td>
                        <td>{0}</td>
                        <td>{1}</td>
                        <td><a class="colorFonts" href="{2}">{2}</a></td>
                        <td>{3}</td>
                    </tr>
                '''.format(dictResults["Date"],
                        str(dictResults["Description"]),
                        dictResults["Download"], str(dictResults["Author"])))
            f.write(r'''
                        </tbody>
                    </table>
                    <hr>
                    <br>
                ''')


        f.write(r'''
    </div>
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="bootstrap/js/bootstrap.min.js"></script>
  </body>
</html>
    ''')

