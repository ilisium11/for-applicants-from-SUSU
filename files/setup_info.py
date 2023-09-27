import pandas as pd
import os
from class_abit import Abitur
from class_direction import Direction
if not os.path.exists('D:/База данных'):
    import create_data
else:
    ls=os.listdir('D:/База данных')
    if 'data.txt' not in ls or 'data1.txt' not in ls:
        import create_data

file=open('D:/База данных/data.txt','r')
directions={}
for i in file:
    info=i.split()
    directions[' '.join(info[:-1])]='https://abit.susu.ru/rating/2023/'+info[-1]
file.close()

file=open('D:/База данных/data1.txt','r')
dict_directions={}
for i in file:
    info=i.split()
    name=' '.join(info[:-6])
    dict_directions[name]=Direction(name,tuple(info[-6:]))
file.close()

dict_applicants= {}
k=0
for direction in directions:
    df = pd.read_html(directions[direction])
    df=df[0]
    numbers=df['№'].tolist()
    applicants=[i.split()[0] for i in df['Абитуриент'].tolist()]
    categories=df['Категория абитуриента'].tolist()
    scores=df['Сумма баллов'].tolist()
    priority=df['Приоритет специальности'].tolist()
    grades=df['Оценки'].tolist()
    for i in range(len(applicants)):
        applicant=applicants[i]
        category=categories[i]
        prior = priority[i]
        sum_grades=sum(int(x) for x in grades[i].split())
        score=scores[i]
        if score==0:
            score=sum_grades
        if applicant not in dict_applicants:
            dict_applicants[applicant]=Abitur(applicant)
            dict_applicants[applicant].add_direction(direction,category,prior,score)
        else:
            dict_applicants[applicant].add_direction(direction,category,prior,score)
    k+=1

for applicant in dict_applicants:
    dict_applicants[applicant].sort_direction()


#36753 - я
#41187 - Матвей
#28289 - Стас
#print(dict_applicants['34538'].list_special)
#print('----------')
