# 리스트
# sort()
a = [1, 2, 5, 4, 3]
b = ['하나', '둘', '셋', '넷', '다섯']
c = ['하나', 2, 3, '넷', '다섯']

a.sort()
print(a)

b.sort()
print(b)

# 에러 : 문자와 숫자 크기 비교 불가
c.sort()
print(c)

# reverse()
a = [1, 2, 5, 4, 3]
b = ['하나', '둘', '셋', '넷', '다섯']
c = ['하나', 2, 3, '넷', '다섯']

a.reverse()
print(a)

b.reverse()
print(b)

c.reverse()
print(c)

# append()
# list.append(value)
# 한번에 하나의 값만 추가 가능
c = ['하나', 2, 3, '넷', '다섯']
c.append('여섯')
c.append(7)
print(c)

# insert()
# 원하는 자리에 값을 추가
# list.insert(index, value)
c.insert(2, '둘')
print(c)

# del
# del list[index]
del c[2]
print(c)

# remove()
# list.remove(value)
c.remove('넷')
print(c)

# 특정 값 찾기
# list[index]
# list.index(value)
# value in list
print(c[4])
print(c.index('하나'))
print('다섯' in c)
print(7 in c)

############################################################
# 튜플
# 비어있는 튜플 : ()
# 값이 하나인 튜플 : (3,), 반드시 마지막에 쉼표
# 같은 값 여러 개 중복 가능
# 값을 변경하거나 삭제 불가능
a = ()
print(a)

b = ('안녕',)
print(b)

c = ('안녕')
print(c)

d = (1, 2, 2, 3, 3, 3)
print(d)

############################################################
# 사전
# key와 value를 1대1로 대응
# {key : value}
# key는 고유의 값을 가져야 함
# key 값에는 리스트 형태는 올 수 있지만 튜플은 올 수 없음
dic = {'name':'구자현', 'birth':'0214', 'ID':2017022023}
print(dic)

a = dic['name']
print(a)

# key 중복 문제, 나중에 입력된 값만 대응
dic = {'one':1, 'one':2, 'three':3}
print(dic)

# key 값으로 list는 불가능
dic = {'name':'구자현', ('1', '2'):'축구'}
print(dic)

dic2 = {'name':'구자현', ('1', '2'):('축구', '농구')}
print(dic2)

dic3 = {'name':'구자현', ('1', '2'):['축구', '농구']}
print(dic3)

dic4 = {'name':'구자현', ['1', '2']:'축구'}
print(dic4)

# 원하는 값 출력하기
dic = {'one':1, 'two':2, 'three':3}
a = dic['two']
print(a)

b = dic.get('three')
print(b)