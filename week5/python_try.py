# try 구문에서 에러가 나면 except 구문을 실행
try:
    a = 1/0
except:
    print("숫자는 0으로 나눌 수 없습니다.")


# 에러의 종류에 따라서 다른 구문을 실행하게 할 수 있다
try:
    a = 1/0
except ZeroDivisionError:
    print("ZeroDivisionError 에러가 날 경우 이 부분 실행")
except:
    print("다른 에러일 경우 이 부분 실행")