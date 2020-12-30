import math

print("숫자를 입력하세요")
# Initialize stuff
s = 0
avg = None
n = 0
maximum = -math.inf
minimum = math.inf
while True:
    num = input()
    if num == "입력 끝":
        break
    num = int(num)
    s += num
    n += 1
    avg = s / n
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"입력 받은 숫자들의 합 : {s}")
print(f"입력 받은 숫자들의 평균 : {avg}")
print(f"가장 큰 숫자 : {maximum}")
print(f"가장 작은 숫자 : {minimum}")
