import os
import sys
keyWords ={"and", "as", "if",
           "default", "default", "as", "like"}
filename = input('소스코드파일명을 입력하세요 ').strip()
if not os.path.isfile(filename):
    print("파일", filename, "이 존재하지 않습니다.")
    sys.exit()
infile = open(filename,'r')
text = infile.read().split()
count = 0
for word in text:
    if word in keyWords:
        count += 1
print(filename, "에", count,'개의 키워드가 포함되어 있습니다.')
