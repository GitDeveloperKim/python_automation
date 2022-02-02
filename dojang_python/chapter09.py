
a = [38, 21, 53, 62, 19]
print(a)

person=['james', 17, 175.3, True]
print(person[::-1])

# range 를 사용하여 list
a = list(range(10, 20, 2))
print(a)

a = tuple(a)
print(a)

# 연습문제
a = list(range(5,-10, -2))
print(a)

# 심사문제
a = int(input())
print(tuple(range(-10, 10, a)))