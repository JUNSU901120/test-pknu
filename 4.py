score = int(input("점수를 입력하세요 : "))

if score >= 90 :
    print("장학생", end='')
else :
    if score >=60 :
        print("합격",end='')
    else :
        print("불합격",end='')

print("입니다. ^^")


## 중첩 if 문을 if ~ elif 문으로 변경

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    print("장학생",end='')

elif score>=60:
    print("합격", end='')

else:

    print("불합격",end='')

print("입니다. ^^")

print()
