__author__ = 'angelinaprisyazhnaya'

import re


def articles_info():
    # если надо конкретный файл, то вот так. если спрашивать индекс языка, то как в HW2 в функции find_articles()
    file = open('tyvwiki-20151002-pages-articles-multistream.xml', 'r', encoding='utf-8')
    dump = file.read().replace('&quot;', '').replace('&lt;', '')
    table = open('table.csv', 'w', encoding='utf-8')

    regex1 = re.compile('<title>(.*?)</title>.*?<text.*?>(.*?)</text>', flags=re.U | re.S)
    regex2 = re.compile('\[\[', flags=re.DOTALL)

    data = regex1.findall(dump)
    i = 0
    table.write('title;links amount;usages amount\n')
    while i < len(data):
        title = data[i][0]
        usages_amount = len(data[i][1].split(' '))
        links = regex2.findall(data[i][1])
        links_amount = len(links)
        table.write(title + ';' + str(links_amount) + ';' + str(usages_amount) + '\n')
        i += 1

    file.close()
    table.close()

# articles_info()

# еще с прошлого задания беда с кодировками при записи в файл
# не знаю, что с этим делать, запуталась
