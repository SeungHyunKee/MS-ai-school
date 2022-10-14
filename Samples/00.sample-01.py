import random

random_number = random.randint(1,100)  # 1에서 100사이의 임의의숫자하나 생성해서 random_number에 저장

# print(random_number)

game_count = 1   # 한번 실패할때마다 game_count는 1씩 증가

while True:

    my_number = int(input("1-100 사이의 숫자를 입력하세요"))    # 입력은 정수형이므로 int 써줌

    if my_number > random_number:
        print('Down!!')
    elif my_number < random_number:              # 파이썬에서는 if + 'elif' 쓴다. 주의하기 elif
        print('Up!!')
    else:
        print(f'축하합니다. {game_count} 번만에 맞추셨습니다.')    # f 를 쓰는이유 ??
        break

    game_count = game_count + 1