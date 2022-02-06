# chapter15 elif를 사용하여 여러 방향으로 분기하기

# 15.4 심사문제: 교통카드 시스템 만들기
age = int(input())
balance = 9000

if 7 <= age <= 12:
    balance -= 650
elif 13 <= age <= 18:
    balance -= 1050
elif age >= 19:
    balance -= 1250

print(balance)