names = input().split()
print("=====\n동이름\n=====")
i = 0
while i < len(names):
    if names[i].endswith("동"):
        print(names[i])
    i += 1