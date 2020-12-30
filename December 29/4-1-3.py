import random

print("로또번호 생성기 프로그램")
count = 1
while count <= 6:
    rd = random.randint(1, 45)
    print(f"{count}번째 번호는 {rd}입니다.")
    count += 1