# # 제어문

# # 조건문 if
# # 조건문 끝에는 항상 ':'콜론 입력
# # 실행문은 반드시 들여쓰기

# # if 조건문1:
# #     실행문1
# # elif 조건문2:
# #     실행문2
# # else:
# #     실행문3

# money = True
# if money == True:
#     print("택시를 탄다")
# else:
#     print("걸어간다")

# # # input()
# # # 입력
# # # 모든 입력값을 문자로 받음

# a = input()
# print(a)

# a = input()
# if a == '있다':
#     print('택시를 타자')
# else:
#     print('걸어 가자')

# age = input()

# if age >= '65':
#     print('고령')
# elif age >= '40':
#     print('중년')
# elif age >= '20':
#     print('청년')
# else:
#     print('미성년')

# # 형변환
# # int(value)
# # float(value)
# # str(value)

# age = int(input())

# if age >= 65:
#     print('고령')
# elif age >= 40:
#     print('중년')
# elif age >= 20:
#     print('청년')
# else:
#     print('미성년')

#############################################################
# # 반복문

# # for 문
# numberlist = ['one', 'two', 'three', 'four', 'five']
# for i in numberlist:
#     print(i)

# add = 0
# for i in range(1, 11):
#     add = add + i

# print(add)

# # while 문
# hi = 0
# while hi < 5:
#     print('안녕')
#     hi += 1

treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit == 10:
        print('나무가 쓰러졌습니다.')