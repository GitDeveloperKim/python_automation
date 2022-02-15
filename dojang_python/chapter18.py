# 18.5 연습문제: 3으로 끝나는 숫자만 출력하기
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i > 73:
        break
    print(i, end=' ')
    i+=1

# 18.6 심사문제: 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력하기
start, stop = map(int, input().split())

i = start

while True:
    if i % 10 == 3:
        i += 1
        continue

    if i > stop:
        break
    print(i, end=' ')
    i += 1


