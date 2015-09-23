__author__ = 'angelinaprisyazhnaya'

import re, time

f = open('long_poem.txt', 'r')
f = f.read()

words = []
f2 = open('words.txt', 'r')

word_list = ''
for line in f2:
    words.append(line.replace('\n', ''))
    word_list += line.replace('\n', '|')

word_list_final = word_list[:-1]

f3 = open('snippets.txt', 'w')

time1 = time.time()

regex = re.compile('(.*?\\n.*?(' + word_list_final + ').*?\\n.*?.*?\\n)')

snippets = regex.findall(f)

i = 0
while i < len(snippets):
    f3.write(snippets[i][0])
    if i % 3 == 2:       #тут я пытаюсь делать пустую строку между сниппетами, но почему-то она получается
        f3.write('\n')   #не через каждые 3 строки, а через каждые 9
    i += 1

time2 = time.time()

time_final = time2 - time1
print(time_final)


##########


f = f.replace('.', '').replace(',', '').replace('!', '').replace('?', '')

rhymes = set()
f4 = open('rhymes.txt', 'w')

time3 = time.time()


regex2 = re.compile('.*?\\s(\\w+)\\n.*?\\s(\\w+)\\n.*?(' + word_list_final + ').*?\\n.*?.*?\\s(\\w+)\\n.*?\\s(\\w+)\\n')
m = regex2.findall(f)

for j in m:
    ending = j[2][-3:]

    if j[0].endswith(ending):
        rhymes.add(j[0])
    if j[1].endswith(ending):
        rhymes.add(j[1])
    if j[3].endswith(ending):
        rhymes.add(j[3])
    if j[4].endswith(ending):
        rhymes.add(j[4])

for i in rhymes:
    f4.write(i + '\n')

time4 = time.time()

time_final2 = time4 - time3
print(time_final2)
