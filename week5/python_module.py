# math 모듈 사용

import math
import re

pi = math.pi


def mycircle(r):
    result = 2 * pi * r
    return result

def myarea(r):
    return pi * math.pow(r, 2)

i = int(input("반지름을 입력하시오 : "))

result1 = mycircle(i)
result2 = myarea(i)

print("둘레는",result1,"넓이는",result2)
print("둘레는 " + str(result1) + " 넓이는 " + str(result2))
print("둘레는 {0} 넓이는 {1}".format(result1, result2))
print("둘레는 %f 넓이는 %f" % (result1, result2))