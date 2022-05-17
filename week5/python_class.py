# 클래스
# self = 만들어낸 객체

class SumCal:
    # 클래스 변수, 생성된 객체의 수량을 파악하기 위함, 모든 객체에게 적용되는 속성
    count = 0
    def __init__(self, num):
        # 인스턴스 변수
        self.result = num
        SumCal.count += 1

    def sum(self, a):
        self.result += a
        return self.result


# 객체 1, 2 생성
myobject = SumCal(0)
myobject2 = SumCal(0)

print(myobject.result)

# 객체 1의 속성만 변경
myobject.result += 1

# 객체 1, 2의 속성 동시 출력
print(myobject.result, myobject2.result)
# 1 0
# 생성된 각 객체는 독립적임을 알 수 있음


# 새로운 객체 생성 
abc = SumCal(4)

# 객체에게 함수 실행
abc.sum(7)

# 변경된 객체의 속성 출력
print(myobject.result, abc.result)

# 생성된 객체의 수 출력
print(SumCal.count)
# 클래스 변수가 객체에도 적용됨을 알 수 있음
print(abc.count)


# 상속

class MinusCal(SumCal):
    def __init__(self, num):
        # 부모 클래스의 속성을 가져오는 두 코드
        SumCal.__init__(self, num)
        # super().__init__(num)
    
    def minus(self, b):
        self.result -= b
        return self.result


cal3 = SumCal(3)
cal4 = SumCal(4)

print(cal3.sum(3))
print(cal4.sum(4))

cal5 = MinusCal(5)
print(cal5.result)
print(cal5.sum(3))
print(cal5.minus(4))