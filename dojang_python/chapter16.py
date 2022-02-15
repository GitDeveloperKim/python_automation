
# 16.5 연습문제
x = [49, -17, 25, 102, 8, 62, 21]
for i in x:
    print(i*10, end=' ')

# 16.6 심사문제: 구구단 출력
x = int(input())
for i in range(1,10):
    print("%d * %d = %d" % (x, i, x*i))