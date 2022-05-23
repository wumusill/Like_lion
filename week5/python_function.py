# 함수

# 함수 사용이유
# 중복된 코드를 줄이자

# 함수의 기본구조
# def 함수명(매개변수):
#     원하는 코드
#     return


def mysum(a, b):
    c = a + b
    print(a, b)
    return c

print(mysum(4, 5))


def mysum_2():
    c = 3 + 5
    return c

print(mysum_2())


# 매개변수에 *을 붙이면 튜플로 받음
def mysum_3(*a):
    print(a)

mysum_3(1, 2, 3, 4)
# (1, 2, 3, 4)


def mysum_4(*a):
    result = 0
    for i in a:
        result += i
    return result

print(mysum_4(1, 2, 3, 4))


# 여러 인자를 받아서 한번에 형변환
a, b, c, d = map(int, input("값을 입력하시오 : ").split())
print(a, b, c, d)


# 전역변수 : 함수 밖에서 정의된 변수
# 지역변수 : 함수 안에서 정의된 변수

a = 2

def sum(num):
    a = num + 1
    return a

print(a)
print(sum(4))
print(a)    # 전역변수에는 변함이 없음을 알 수 있음


a = 2

def sum_2(num):
    global a    # 전역변수를 사용하겠다고 선언
    a = num + 1
    return a

print(a)
print(sum_2(4))
print(a)    # 전역변수 변화


# 리스트, 셋, 딕셔너리는 가변 변수로 함수에 별도 선언 없이 전역변수 사용 가능
b = [1, 2, 3, "안녕"]

def myfunction(list):
    list.append(8)
    list.remove(1)
    return list

print(b)
print(myfunction(b))
print(b)


def gugudan(num):
    print("구구단은 " + str(num) + "단입니다.")
    for i in range(1, 10):
        print("{} * {} = {}".format(num, i, num * i))

a = int(input("몇단을 출력할까요? : "))
gugudan(a)