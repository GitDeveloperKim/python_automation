print('hello world')

a = list(range(0,100,10))
print(a[:7:2])
print(len(a))
del a[2:5]
print(a)

b='hello, world!'
print(b[2:])
print(b[:9:2])

# 연습문제 11.6
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])

# 연습문제 11.7 홀수인 요소 출력
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

# 심사 문제 : 리스트의 마지막 부분 삭제하기
#x = list(input().split(" "))
#print(tuple(x[:-5]))

a = input()
b = input()
print(a[1::2] + b[::2])
