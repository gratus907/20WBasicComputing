import pandas as pd

names = input("학생들의 이름 입력(,로 구분): ").split(',')
score_kor = list(map(int, input("학생들의 국어성적 입력(,로 구분): ").split(',')))
score_eng = list(map(int, input("학생들의 영어성적 입력(,로 구분): ").split(',')))
score_mat = list(map(int, input("학생들의 수학성적 입력(,로 구분): ").split(',')))

print()
dF = pd.DataFrame(index = names)
dF['국어'] = score_kor
dF['영어'] = score_eng
dF['수학'] = score_mat
dF['합계'] = dF.sum(axis = 1)
dF.loc['평균'] = dF.sum(axis = 0)//3
print(dF)

search = input("검색할 학생 이름은? ")
print()
print(dF.loc[search])
