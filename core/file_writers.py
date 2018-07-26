import os
import webbrowser
import sys
import subprocess


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
    html = ''.join(open("common/html_page/base.html", "r").readlines())
    data = __helper_write_html(dict_all_results)
    final_html = html.format(word_search=data["word_search"],
                             list_dict_result=data["table_rows"])

    with open(r"out.html", "w") as f:
        f.write(final_html)


def __helper_write_html(iterable_data):
    data_result = {}
    table_rows = ""

    for word_search, list_results in iterable_data.items():
        table_rows += r"""
        <br>
        <h3 style="color:lime;"> Results for search:  {0}</h3>
        <br>
        <table style="color:lime"; border="1">
            <thead>
                <tr>
                    <td></td>
                    <th>Date </th>
                    <th>Description</th>
                    <th>Url</th>
                </tr>
            </thead>
            <tbody>
        """.format(word_search)
        for dict_result in list_results:
            for key, result in dict_result.items():
                for exploit_data in result:
                    data_result["word_search"] = word_search
                    table_rows += r"""
                        <tr>
                            <td></td>
                            <td>{0}</td>
                            <td>{1}</td>
                            <td><a style="color:lime;" id="url_download" href="{2}" target='_blank'>{2}</a></td>
                        </tr>
                    """.format(exploit_data["date"],
                               str(exploit_data["name"]),
                               exploit_data["url"], )
        table_rows += """
                    </tbody>
                </table>
        """
    data_result["table_rows"] = table_rows
    return data_result


def open_url(url):
    webbrowser.open(url)

def write_txt(dict_all_results):
    """
        Write result in file out.txt for better viewing.
    """
    with open("out.txt", "w") as f:
        f.write("date;description;url\n")
        for word_search, list_results in dict_all_results.items():
                for dict_result in list_results:
                    for key, result in dict_result.items():
                        for exploit_data in result:
                            f.write("{0};{1};{2}\n".format(
                                exploit_data["date"],
                                str(exploit_data["name"]),
                                exploit_data["url"])
                            )