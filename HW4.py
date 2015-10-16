__author__ = 'angelinaprisyazhnaya'

import re
import sqlite3


def articles_info():
    # если надо конкретный файл, то вот так. если спрашивать индекс языка, то как в HW2 в функции find_articles()
    file = open('chywiki-20150901-pages-articles-multistream.xml', 'r', encoding='utf-8')
    dump = file.read().replace('&quot;', '').replace('&lt;', '')

    regex1 = re.compile('<title>([^:]*?)</title>.*?<text.*?>(.*?)</text>', flags=re.U | re.S)

    data = regex1.findall(dump)
    file.close()
    return data


def dbwrite(data):
    connection = sqlite3.connect('HW4.db')
    c = connection.cursor()
    connection.execute('''CREATE TABLE HW4 (word TEXT, usages INT)''')

    i = 0
    regex2 = re.compile('\\w+')
    regex3 = re.compile('#|,|\.|\{|:|\(|\)|\}|\]|\[|;|=|&|\||!|\?|\"|\'|/|_')
    while i < len(data):
        words = data[i][1].split(' ')
        for word in words:
            if regex2.search(word) is not None:
                word = regex3.sub('', word)
                c.execute('''SELECT * FROM HW4 WHERE word=?''', (word,))
                match = c.fetchone()
                if match is None:
                    connection.execute('''INSERT INTO HW4 VALUES (?,'1')''', (word,))
                    connection.commit()
                else:
                    print(match)
                    amount = match[1]
                    amount += 1
                    c.execute("UPDATE HW4 SET usages=? WHERE word=?", (amount, word))
                    connection.commit()
            else:
                continue
        i += 1

dbwrite(articles_info())
