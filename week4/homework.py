# 1번
Hurdle = 0

for i in range(5):
    print("허들을 넘었습니다.")
    Hurdle += 1
    if Hurdle == 5:
        print("레이스를 완주했습니다.")


# 2번
Hurdle = 5

while Hurdle > 0:
    print("허들이 %d개 남았습니다." %Hurdle)
    Hurdle -= 1
print("레이스를 완주했습니다.")


# 3번
name = input()
score = int(input())

if score in range(90, 101):
    grade = "A"
elif score in range(80, 90):
    grade = "B"
elif score in range(70, 80):
    grade = "C"
elif score in range(60, 70):
    grade = "D"
else:
    grade = "F"

print("{}의 학점 : {}".format(name, grade))


# 4번
for _ in range(4):
    name = input()
    score = int(input())

    if score in range(90, 101):
        grade = "A"
    elif score in range(80, 90):
        grade = "B"
    elif score in range(70, 80):
        grade = "C"
    elif score in range(60, 70):
        grade = "D"
    else:
        grade = "F"

    print("{}의 학점 : {}".format(name, grade))