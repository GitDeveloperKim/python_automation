# else 를 사용하여 두방향으로 분기하기

# 14.7 심사문제: 합격 여부 판단하기
(korean, english, mathematics, science) = map(int, input().split())
sum = korean + english + mathematics + science
avg = sum/4

if (0 <= korean <= 100) and (0 <= english <= 100) and \
    (0 <= mathematics <= 100) and (0 <= science <= 100):
    if avg >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')


'''먼저 국어, 영어, 수학, 과학 점수가 한 줄에 입력되므로 input에서 split을 사용한 뒤
 변수 네 개에 저장해주면 됩니다(변수는 이하 korean, english, mathematics, science). 이
 때 input().split()의 결과는 문자열 상태이므로 map에 int를 사용하여 정수로 변환해줍니다.

먼저 점수는 0점부터 100점까지만 입력받을 수 있다고 했으므로 if 조건문을 사용하여
 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathematics <= 100 and 0 <= science <= 100과 같이
  모든 점수가 0점 이상이거나 100점 이하인지 검사해야 합니다. 
  특히 하나라도 범위를 벗어나면 안 되므로 모두 and 연산자로 판단합니다. 
  점수가 범위 안에 있으면 if 부분에서 합격 불합격 여부를 판단하고, 
  점수가 범위를 벗어나면 else 부분에서 print로 '잘못된 점수'를 출력합니다
  (if 부분에 합격, 불합격을 판단하는 if, else가 들어감).

또는, korean < 0 or korean > 100 or english < 0 or english > 100 
or mathematics < 0 or mathematics > 100 or science < 0 or science > 100
처럼 모든 점수가 0점 미만이거나 100점 초과인지 검사합니다. 
이때는 하나라도 범위를 벗어나면 잘못된 점수이므로 or 연산자로 판단합니다. 
그리고 if 부분에서 '잘못된 점수'를 출력하고, else 부분에서 합격 불합격 여부를 판단해도 됩니다.

합격, 불합격 여부는 국어, 영어, 수학, 과학 점수의 평균이 80점 이상이라야 합격이므로 
(korean + english + mathematics + science) / 4 >= 80과 같이 
조건문 안에서 평균을 구하고 80점 이상인지 검사합니다. 
그리고 if 부분에는 print로 '합격'을 출력하고,
 else 부분에는 '불합격'을 출력하면 됩니다. 
 여기서 주의할 점이 있는데 평균을 구할 때는 반드시 덧셈 부분을 괄호로 묶어야 합니다. 
 괄호로 묶지 않으면 나눗셈이 먼저 계산되어 잘못된 결과가 나옵니다.

이처럼 프로그램을 만들 때는 입력 값의 범위를 항상 확인하는 것이 좋습니다. 
범위를 벗어난 입력 값으로 인해 완전히 잘못된 값이 나올 수 있고, 
상당수의 보안 취약점이 입력 값의 범위를 검사하지 않아서 발생하게 됩니다.'''