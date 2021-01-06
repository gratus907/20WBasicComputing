import random

color = ['black', 'grey', 'white', 'pink', 'orange']
topwears = ['sweater', 'shirts', 'blouse', 'jacket']
bottomwears = ['skirt', 'pants', 'leggings', 'jeans']
accessory = ['hat', 'tie', 'scarf', 'shoes']

for i in range(3):
    print(f"오늘의 패션 {i + 1}번 추천 조합입니다.")
    print(f"{random.choice(color)} {random.choice(topwears)}")
    print(f"{random.choice(color)} {random.choice(bottomwears)}")
    print(f"{random.choice(color)} {random.choice(accessory)}")
    print()