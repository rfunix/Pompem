# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

from BeautifulSoup import BeautifulStoneSoup
import requests
import os


class DownloadPage(object):

    def __init__(self, url=None):
        self.url = url
        self.__headers = {
            'User-Agent': 'Googlebot/2.1 (+http://www.googlebot.com/bot.html)'
        }

    def get_download_page(self, host=None, parametros=None):
        try:

            if ("exploit-db" in host):
                r = requests.get(
                    host, params=parametros, headers=self.__headers, verify=False)
            else:
                r = requests.get(
                    host, params=parametros, headers=self.__headers)

            decodedstring = BeautifulStoneSoup(
                r.text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
            return str(decodedstring)
        except Exception, e:
            print(e.message)
            return None

    def post_download_page_day(self, host=None, postData={}):
        s = requests.session()
        s.post(host, headers=self.__headers, data={"agree": "Yes, I agree"})
        r = s.get(host, headers=self.__headers, data=postData)
        decodedstring = BeautifulStoneSoup(
            r.text, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)
        return decodedstring


def download_file(url, directory):
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


def write_txt(dict_all_results):
    """
        Write result in file out.txt for better viewing.
    """
    for word_search, list_results in dict_all_results.items():
        if not list_results[0]:
            continue
        with open("out.txt", "w") as f:
            f.write("+" + "-" * 150 + "+\n")
            f.write("+Results {0}\n".format(word_search))
            f.write("+" + "-" * 150 + "+\n")
            f.write(
                "+Date            Description" +
                "                                     Download" +
                "                                       Author\n")
            f.write("+" + "-" * 150 + "+\n")
            for listDictResults in list_results:
                for dictResults in listDictResults:
                    f.write("+ {0} | {1} | {2} | {3} \n".format(
                        dictResults["Date"],
                        str(dictResults["Description"]),
                        dictResults["Download"], str(dictResults["Author"])
                    )
                    )
                    f.write("+" + "-" * 150 + "+\n")


def write_html(dict_all_results):
    """
        The write_html method read file base.html and stores in the variable
        ::html. In the file base.html we have two keys for usage later in
        my_string.format(). These two keys are: word_search and list_dict_results.
        We use the method __helper_write_html() for get data for these keys.
        The file base.html can't internal style sheet because the your syntax
        uses the { and } characters, making the location of the keys mentioned 
        above by the method format() string type. For this reason the internal 
        style sheets were modified for the inline style sheet on html. 
    """
    html = ''.join(open("engine/html/base.html", "r").readlines())
    data = __helper_write_html(dict_all_results)
    final_html = html.format(word_search=data["word_search"],
                             list_dict_result=data["table_rows"])

    with open(r"out.html", "w") as f:
        f.write(final_html)


def __helper_write_html(iterable_data):
    data_result = {}
    table_rows = ""

    for word_search, list_results in iterable_data.items():
        if not list_results[0]:
            continue

        data_result["word_search"] = word_search
        for list_dict_results in list_results:
            for dict_results in list_dict_results:
                table_rows += r"""
                    <tr>
                        <td></td>
                        <td>{0}</td>
                        <td>{1}</td>
                        <td><a style="color:lime;" href="{2}">{2}</a></td>
                        <td>{3}</td>
                    </tr><br/>
                """.format(dict_results["Date"],
                           str(dict_results["Description"]),
                           dict_results["Download"], str(dict_results["Author"]))
    data_result["table_rows"] = table_rows
    return data_result
