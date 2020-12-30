import random

print("이번 주 컴또복권\n")
total = 0

while True:
    lottery = list(map(int, input("네 개의 숫자를 입력하세요: ").split()))

    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chosen = []
    while len(chosen) < 4:
        randomIndex = random.randint(0, len(candidates)-1)
        num = candidates[randomIndex]
        del candidates[randomIndex]
        chosen.append(num)
    i = 0
    correct = []
    while i < len(lottery):
        if lottery[i] in chosen:
            correct.append(lottery[i])
        i += 1
    print(f"맞춘 숫자는 {correct}입니다.")
    if len(correct) == 4:
        print("4개를 맞춰 당첨금은 10000원입니다.")
        total += 10000
    elif len(correct) == 3:
        print("3개를 맞춰 당첨금은 5000원입니다.")
        total += 5000
    else:
        print("당첨되지 않았습니다. 다음 기회에...")

    replay = input("또 하시겠습니까? ")
    if replay.startswith('n') or replay.startswith('N'):
        print(f"총 당첨금은 {total}원입니다.")
        break
