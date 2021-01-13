import pandas as pd

names = []
infos = []

while True:
    name = input("고객의 이름: ")
    if name == '':
        break
    gender = input("고객의 성별(남/여) ")
    age = int(input("고객의 나이: "))
    job = input("고객의 직업(학생/직장인/자영업/전문직/기타): ")
    info = (gender, age, job)
    names.append(name)
    infos.append(info)

dF = pd.DataFrame(infos, index=names, columns=['성별', '나이', '직업'])

female_seniors = dF[(dF.나이 >= 60) & (dF.성별 == '여')]
students = dF[(dF.직업 == '학생')]
middle_ages = dF[(dF.나이 >= 30) & (dF.나이 < 50)]
print('===================================')
print('고객 명단: ')
print(dF)
print('-----------------------------------')
print('나이가 60 이상인 여성 고객 명단: ')
print(female_seniors)
print('-----------------------------------')
print('직업이 학생인 고객 명단: ')
print(students)
print('-----------------------------------')
print('30, 40대 고객 명단: ')
print(middle_ages)
