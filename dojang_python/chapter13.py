# if 조건문으로 특정 조건일 때 코드 실행하기

# 13.7 심사문제: 온라인 할인 쿠폰 시스템 만들기
cash = int(input())
discount = input()

if discount == 'Cash3000':
    cash -= 3000
elif discount == 'Cash5000':
    cash -= 5000

print(cash)