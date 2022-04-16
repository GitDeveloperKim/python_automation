# chapter 20 Fizz Buzz 문제
# 20.7 연습 문제
for i in range(1, 101) :
    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')
    elif i % 2 == 0:
        print('Fizz')
    elif i % 11 == 0:
        print('Buzz')
    else:
        print(i)

# 20.8 심사 문제
# 먼저 정수 두 개가 한 줄에 입력되므로 input에서 split을 사용한 뒤 변수 두 개에 저장해주면 됩니다(변수는 이하 start, stop).
# 이때 input().split()의 결과는 문자열 상태이므로 map에 int를 사용하여 정수로 변환해줍니다.
start, stop = map(int, input().split(' '))

for i in range(start,stop+1):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)