# 1번
def plus(num_1, num_2):
    return num_1 + num_2

def minus(num_1, num_2):
    return num_1 - num_2

def multi(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

while True:
    num_1, num_2 = map(int, input("연산을 진행할 두 숫자를 입력하시오 : ").split())
    cmd = input("어떠한 연산을 수행할까요? ")

    if cmd == '+':
        print("{} {} {} = {}\n".format(num_1, cmd, num_2, plus(num_1, num_2)))
    
    elif cmd == '-':
        print("{} {} {} = {}\n".format(num_1, cmd, num_2, minus(num_1, num_2)))
    
    elif cmd == '*':
        print("{} {} {} = {}\n".format(num_1, cmd, num_2, multi(num_1, num_2)))
    
    elif cmd == '/':
        print("{} {} {} = {}\n".format(num_1, cmd, num_2, divide(num_1, num_2)))
    
    else:
        print("해당 연산은 지원하지 않습니다.\n")

    
# 2번
import random
import time

def lotto():
    lotto_nums = []
    while len(lotto_nums) < 6:
        num = random.randint(1, 45)
        if num not in lotto_nums:
            lotto_nums.append(num)
    lotto_nums.sort()
    return lotto_nums

while True:
    respond = input('로또번호 추출을 시작합니까? (y/n) : ')
    if respond == 'y':
        print("번호 추출중...")

        for i in range(1, 6):
            time.sleep(1)
            print("{}...".format(i))
        
        print("로또 번호는!!\n")
        print("{} 입니다.".format(lotto()))

    else:
        print("로또 추출을 종료합니다.")
        break