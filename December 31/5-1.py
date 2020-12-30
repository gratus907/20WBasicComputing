print("상품재고관리 프로그램")
prompt = "상품관리(1. 삽입, 2.삭제, 3.상품 확인, 4.종료):"
prodList = ["커피", "우유", "바나나", "감귤", "화장지",
            "장갑", "이불", "베개", "장난감", "음료수", "빵"]
while True:
    print()
    op = int(input(prompt))
    if op == 1:
        prodName = input("상품관리1-삽입) 삽입하고자 하는 상품은?")
        position = int(input("상품관리1-삽입) 삽입하고자 하는 위치는?"))
        prodList.insert(position, prodName)
        print(f"{prodName} 삽입 완료")
        print(prodList)
    elif op == 2:
        prodName = input("상품관리2-삭제) 삭제하고자 하는 상품은?")
        if prodName in prodList:
            prodList.remove(prodName)
            print(f"{prodName} 삭제 완료")
            print(prodList)
        else:
            print("상품을 찾지 못하였습니다.")
    elif op == 3:
        prodName = input("상품관리3-상품 확인) 확인하고자 하는 상품은?")
        if prodName in prodList:
            print(f"{prodName} 검색 완료")
            print(prodList)
        else:
            print("상품을 찾지 못하였습니다.")
    elif op == 4:
        break
print("프로그램을 종료합니다")