# chapter 22 리스트와 튜플 응용하기

# 예시도 풀어볼 것

# 22.9 연습문제 : 리스트에서 특정 요소만 뽑아내기
a = ['alpha', 'bravo', 'charlie','delta','echo', 'foxtrot','golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

# 22.10
a, b = map(int, input().split(' '))
x = [pow(2,i) for i in range(a,b+1) if not (i == a+1 or i == b-1)]
print(x)

'''
해설

먼저 정수 두 개가 한 줄에 입력되므로 input에서 split을 사용한 뒤 변수 두 개에 저장해주면 됩니다(변수는 이하 start, stop). 

이때 input().split()의 결과는 문자열 상태이므로 map에 int를 사용하여 정수로 변환해줍니다.

첫 번째 정수에서 두 번째 정수까지 숫자를 생성하려면 for i in range(start, stop + 1)처럼 반복문을 작성합니다. 

그리고 이 반복문으로 2의 거듭제곱 리스트를 생성하려면 [2 ** i for i in range(start, stop + 1)]과 같이 작성하면 됩니다.

그리고 리스트의 두 번째 요소와 뒤에서 두 번째 요소를 삭제하라고 했으므로 리스트에서 pop(1)을 사용하여 두 번째 요소를 삭제하고, 

pop(-2)를 사용하여 뒤에서 두 번째 요소를 삭제합니다. 또는, del a[1], del a[-2]로 요소를 삭제해도 됩니다.

마지막으로 print로 리스트를 출력해줍니다.
'''