import random
proverb = [
    '꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.',
    '고생없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.',
    '사람은 사랑할 때 누구나 시인이 된다.',
    '시작이 반이다.',
    '나는 사랑으로 내가 이해하는 모든 것들을 이해한다.'
]
print('========================')
print(' 오늘의 명언 ')
print('========================')
rand_index = random.randint(0, len(proverb) - 1)
print(proverb[rand_index])