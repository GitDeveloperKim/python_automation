# else 를 사용하여 두방향으로 분기하기

# 14.7 심사문제: 합격 여부 판단하기
sum = 0
x = list(map(int, input().split()))

check = True
for a in x:
    if a > 100 or a < 0:
        print('잘못된 점수')
        check = False
    sum += a
avg = sum/4

if check:
    if avg >= 80:
        print('합격')
    else:
        print('불합격')