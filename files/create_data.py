from bs4 import BeautifulSoup
import requests
import os
url='https://abit.susu.ru/rating/2023/bachelor-intra.php'
r=requests.get(url)
page=BeautifulSoup(r.text,'lxml')
table = page.find('table')


readlines=[]


def create_abbreviation(tx):
    for char in (':', ';', ',', '-'):
        if char in tx:
            tx = tx.replace(char, ' ')
    if '(' in tx:
        ind = tx.find('(')
        tx = tx[:ind]
    b = tx.split('.')
    b = [element.split() for element in b]
    for j in b:
        for char in ('для', 'и'):
            if char in j:
                j.remove(char)
    name=''
    for element in b:
        name+=''.join(word[0].upper() for word in element)
        name+=' '
    return name


for i in table.find_all('tr')[1:]:
    info=i.find_all('td')
    name_special=''.join(info[1].text)
    ls=name_special.split()
    num=ls[0]
    special_text=' '.join(ls[1:])
    link=info[5].find('a')
    if link:
        readlines.append((create_abbreviation(info[0].text)+' '+name_special.split()[0]+' '+create_abbreviation(special_text),link.get('href')))


def kvo(tex):
    tx=tex
    text1='Целевая квота: '
    target_kvo='0'
    if text1 in tx:
        ind=tx.index(text1)+len(text1)
        if tx[ind+1]!=';':
            target_kvo=tx[ind:ind+2]
        else:
            target_kvo=tx[ind]

    text1 = 'Особая квота: '
    special_kvo='0'
    if text1 in tx:
        ind=tx.index(text1)+len(text1)
        if tx[ind+1]!=';':
            special_kvo=tx[ind:ind+2]
        else:
            special_kvo=tx[ind]

    text1 = 'Отдельная квота: '
    separate_kvo='0'
    if text1 in tx:
        ind=tx.index(text1)+len(text1)
        if tx[ind+1]!=';':
            separate_kvo=tx[ind:ind+2]
        else:
            separate_kvo=tx[ind]
        separate_kvo=separate_kvo.strip()

    text1='Совмещенная квота (особая, целевая): '
    combo_kvo='0'
    if text1 in tx:
        ind=tx.index(text1)+len(text1)
        if tx[ind+1]!=';':
            combo_kvo=tx[ind:ind+2]
        else:
            combo_kvo=tx[ind]

    text1 = 'Совмещенная квота (отдельная, целевая): '
    combo_kvo1='0'
    if text1 in tx:
        ind=tx.index(text1)+len(text1)
        if tx[ind+1]!=';':
            combo_kvo1=tx[ind:ind+2]
        else:
            combo_kvo1=tx[ind]
        combo_kvo1=combo_kvo1.strip()
    return target_kvo,special_kvo,separate_kvo,combo_kvo,combo_kvo1


os.mkdir('D:/База данных')
file=open('D:/База данных/data.txt','w')
file1=open('D:/База данных/data1.txt','w')
readlines_places=[]
for i in readlines:
    url='https://abit.susu.ru/rating/2023/'+i[1]
    site=requests.get(url)
    page=BeautifulSoup(site.text,'lxml')
    text=page.find_all('p')[1].text
    total=int(text.split()[4][:-1])
    all_kvo=kvo(text)
    sum_kvo=sum(int(x) for x in all_kvo)
    file.write(i[0]+' '+i[1]+'\n')
    file1.write(i[0]+' '+str(total-sum_kvo)+' '+' '.join(all_kvo)+'\n')

file.close()
file1.close()

