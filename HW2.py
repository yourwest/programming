__author__ = 'angelinaprisyazhnaya'

import urllib.request as urlr
import re
import os

def load_dump():
    lang_index = input('Input an index: ')

    page1 = urlr.urlopen('https://dumps.wikimedia.org/backup-index.html')
    all_dumps = page1.read().decode('utf-8')

    m = re.search('<a\\shref="(' + lang_index + 'wiki/\\d{8})">', all_dumps, flags=re.DOTALL)
    if m is not None:
        url = 'https://dumps.wikimedia.org/' + m.group(1) + '/'

        page2 = urlr.urlopen(url)
        lang_dumps = page2.read().decode('utf-8')

        m = re.search('<ul><li\\sclass=\'file\'><a\\shref="(.*?)">(.*?)</a>', lang_dumps, flags=re.DOTALL)
        if m is not None:
            dump_url = 'https://dumps.wikimedia.org/' + m.group(1)
            file_name = m.group(2)
            urlr.urlretrieve(dump_url, file_name)
        else:
            print('Not found')

    else:
        print('Not found')


def find_articles():
    lang_index = input('Input an index: ')
    path = os.getcwd()
    file_names = os.listdir(path)
    file_name = ''

    for file in file_names:
        if file.startswith(lang_index + 'wiki'):
            file_name = file
            dump = open(file_name, 'r')
            dump = dump.read().replace('&quot;', '')
            articles = open('article_names.txt', 'w')

            titles = re.findall('<title>(.*?)</title>', dump, flags=re.DOTALL)
            i = 0
            titles = sorted(titles)
            while i < len(titles):
                articles.write(titles[i] + '\n')
                i += 1
            break

    if file_name == '':
        print('Not found')

#load_dump()
#find_articles()
