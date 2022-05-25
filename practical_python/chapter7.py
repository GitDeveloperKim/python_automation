import re

phoneNumRegex = re.compile(r'(\d{3})-(\d{4})-(\d{4})')
mobile = phoneNumRegex.search('My number is 010-0000-0000') # 없으면 None
if mobile is not None:
    print('phone number found: ' + mobile.group()) # 실제 패턴 문자열 리턴
    print('phone number found: ' + mobile.group(0))
    print('phone number found: ' + mobile.group(1))
    print('phone number found: ' + mobile.group(2))
    print('phone number found: ' + mobile.group(3))

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina')
print(mo1.group()) # Batman
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group()) # Tina Fey (뒤에 맞은 문자는 무시 한다)

print("선택적 ?")
heroRegex = re.compile(r'Bat(wo)?man') # wo 는 선택적 패턴
mo1 = heroRegex.search('Batman')
print(mo1.group())
mo2 = heroRegex.search('Batwoman')
print(mo2.group())

print("* <-- 0개 또는 그 이상과 일치 시키기")
heroRegex = re.compile(r'Bat(wo)*man') # wo 는 선택적 패턴
mo1 = heroRegex.search('Batwowowoman')
print(mo1.group())
mo2 = heroRegex.search('Batwoman')
print(mo2.group())

print("+ <-- 하나 또는 그 이상과 일치 시키기")
heroRegex = re.compile(r'Bat(wo)+man') # wo 는 선택적 패턴
mo1 = heroRegex.search('Batwowowoman')
print(mo1.group())
mo2 = heroRegex.search('Batman')
print(mo2 is None)

print("대괄호 -> 사용자 정의 문자 클래스")
vowelRegex = re.compile(r'[aeiouAEIOU]') # 모음 찾기
print (vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))

print("시작 기호 ^ (캐럿)")
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print (vowelRegex.findall('RoboCop eats baby food. BABY FOOD'))

print("$ 끝남 기호 달러")
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') is None)
print(wholeStringIsNum.search('12    34567890') is None)


print(". <-- 와일드 카드 문자 (줄바꿈 제외한 모든문자)")
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

print("점 별표로 모든것 일치")
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print (mo.group(1))
print (mo.group(2))

print("sub 메소드로 문자열 대체하기")
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))