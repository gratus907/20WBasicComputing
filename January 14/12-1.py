import pandas as pd

names = input("학생들의 이름 입력(,로 구분): ").split(',')
score_kor = list(map(int, input("학생들의 국어성적 입력(,로 구분): ").split(',')))
score_eng = list(map(int, input("학생들의 영어성적 입력(,로 구분): ").split(',')))
score_mat = list(map(int, input("학생들의 수학성적 입력(,로 구분): ").split(',')))

ser_kor = pd.Series(score_kor, index = names)
ser_eng = pd.Series(score_eng, index = names)
ser_mat = pd.Series(score_mat, index = names)

ser_sum = ser_kor + ser_eng + ser_mat

print("\n국어성적")
print(ser_kor)
print("영어성적")
print(ser_eng)
print("수학성적")
print(ser_mat)
print("합계")
print(ser_sum)