import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', '587')
print(type(smtpObj))

# smtp 서버에 인사하기
print(smtpObj.ehlo())

# smtp tls 암호화
print(smtpObj.starttls())

# smtp
id = input()
pwd = input()
sendMail = input()
print(smtpObj.login(id, pwd))

# 구글 계정 설정하기 참고
# https://yeolco.tistory.com/93
smtpObj.sendmail(id, sendMail, 'msg')
smtpObj.quit()