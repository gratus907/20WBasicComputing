koreng = dict()

def add_word():
    kor = input("등록할 한국어 단어 입력: ")
    eng = input("등록할 영어 단어 입력: ")
    koreng[kor] = eng

def find_eng():
    kor = input("검색할 단어: ")
    print(f"영어 : {koreng[kor]}")

def find_kor():
    eng = input("검색할 단어: ")
    for key in koreng.keys():
        if koreng[key] == eng:
            print(f"한국어 : {key}")

menu = 0
print("----------------------------메뉴----------------------------")
print("1. 단어 등록   2. 한국어 -> 영어   3. 영어 -> 한국어   4. 종료")
print("------------------------------------------------------------")
while menu != 4:
    menu = int(input("메뉴를 선택하세요: "))
    if menu == 1:
        add_word()
    elif menu == 2:
        find_eng()
    elif menu == 3:
        find_kor()
    else:
        pass
    print()

print("프로그램을 종료합니다.")