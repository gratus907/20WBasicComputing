correctPassword = "pythonisfun"
password = ""
trial = 0
while True:
    print("암호를 입력하세요.")
    password = input()
    trial += 1
    if password == correctPassword:
        print("로그인 성공")
        break
    if trial >= 5:
        print("5회 틀렸습니다. 로그인에 실패하셨습니다.")
        break