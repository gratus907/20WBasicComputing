storage = {
    "커피" : 7,
    "펜" : 3,
    "종이컵" : 2,
    "우유" : 1,
    "콜라" : 5,
    "책" : 5
}

pp = {
    "커피" : "는",
    "펜" : "은",
    "종이컵" : "은",
    "우유" : "는",
    "콜라" : "는",
    "책" : "은"
}

def check_storage():
    item = input("물건명 입력: ")
    print(f"{item}{pp[item]} {storage[item]}개 남았습니다.")

def sell_item():
    item = input("물건명 입력: ")
    quantity = int(input(f"{item}의 판매 개수: "))
    storage[item] -= quantity
    print(f"{item}{pp[item]} {storage[item]}개 남았습니다.")

menu = 0
while menu != 3:
    print("-------------메뉴-------------")
    print("1. 재고확인   2. 판매   3. 종료")
    print("-----------------------------")
    menu = int(input("메뉴를 선택하세요: "))
    if menu == 1:
        check_storage()
    elif menu == 2:
        sell_item()
    else:
        pass
    print()