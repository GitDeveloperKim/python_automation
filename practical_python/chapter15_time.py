'''
time, date 모듈
웹사이트 변경사항 체크를 위해 1시간 마다 긁어오기
새벽에 컴퓨터 돌리기
subprocess, threading
미리 정한 일정에 따라 다른 프로그램을 실행 시킨다
'''

import time
# time() 성능 분석에 사용
def calcProd():
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime)) #시간 출력 부분

# time.sleep() : 프로그램 일시 정지상태 초단위
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

# datetime : 더욱 편리한 형식으로 날짜를 표시하거나 날짜로 산술 연산 (컴퓨터 내장 시계 기준)
import datetime
print(datetime.datetime.now())
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(dt.year, dt.minute, dt.day)

halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
print(halloween2015 > newyears2016) # 나중 날짜일수록 크다 : false
print(newyears2016 > halloween2015) # True
print(halloween2015 == oct31_2015) # True

# time delta 시간의 기간을 표현하는 유형
dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)
print(dt - thousandDays)

# 위 time delta 를 이용하면 특정날짜까지 일시정지 시킬 수 있다
#p392

#datetime 객체를 문자열로 변환하기 (strftime) -> string format time
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))

#문자열을 datetime 객체로 변환하기 (strptime) -> string parse time
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))

# 파이썬에서 다른 프로그램 실행하기
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')