import random

def check(hidden, guess):
    st = 0
    ba = 0
    for i in range(3):
        if hidden[i] == guess[i]:
            st += 1
        elif guess[i] in hidden:
            ba += 1
    return st, ba

hidden = random.sample(range(10), 3)
for i in range(10):
    guess = list(map(int, input("숫자 3개를 입력하세요. (예: '3 5 8') ").split()))
    s, b = check(hidden, guess)
    if s == 3:
        print("Home run\n게임을 종료합니다.")
        break
    else:
        print(f"{s} strike {b} ball")
else:
    print(f"기회를 모두 소진하였습니다. 비밀숫자는 {hidden} 입니다.")