
# 17.4 퀴즈
i = 10
while i < 19:
    print(i, end=' ')
    i+=2

# 17.5 연습문제: 변수 두개를 다르게 반복하기
i = 2
j = 5

while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1

# 17.6 심사문제 : 교통카드 잔액 출력하기
balance = int(input())

while balance-1350 >= 0:
    balance -= 1350
    print(balance)
