import pandas as pd


names = input("학생들의 이름 입력(,로 구분): ").split(',')
score_kor = list(map(int, input("학생들의 국어성적 입력(,로 구분): ").split(',')))
score_eng = list(map(int, input("학생들의 영어성적 입력(,로 구분): ").split(',')))
score_mat = list(map(int, input("학생들의 수학성적 입력(,로 구분): ").split(',')))

dF = pd.DataFrame(index = names)
dF['국어'] = score_kor
dF['영어'] = score_eng
dF['수학'] = score_mat
dF['합계'] = dF.sum(axis = 1)

print()
print(dF)

sort_by = input('정렬 기준 선택 (1:국어, 2:영어, 3:수학, 4:합계): ')
sort_type = input('정렬 방법 선택 (1:오름차순, 2:내림차순): ')
if sort_by == "1" :
    sort_criteria = '국어'
elif sort_by == "2" :
    sort_criteria = '영어'
elif sort_by == "3" :
    sort_criteria = '수학'
else :
    sort_criteria = '합계'

if sort_type == "1" :
    sort_type = True
else :
    sort_type = False

sorted_dF = dF.sort_values(by = sort_criteria, ascending = sort_type)
print()
print(sorted_dF)
