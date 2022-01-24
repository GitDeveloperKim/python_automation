# chapter7
#quiz 1
print(3.1, 'python', 100)

#quiz 2
print(16, 9, sep=':')

#quiz 3
print('Hello', '\n', 'Python', sep='')

#pracice 1
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

#dojang
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')