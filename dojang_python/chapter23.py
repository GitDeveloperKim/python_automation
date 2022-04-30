a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

# 연습문제: 3차원 리스트 만들기
a = [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]
print(a)