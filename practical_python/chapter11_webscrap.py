# webbrowser : 파이썬과 함께 제공되는 모듈로서 웹브라우저로 특정 페이지를 연다
# requests : 인터넷에서 파일과 웹페이지를 다운로드한다
# beautiful soup : 웹 페이지를 작성하는 형식인 HTML을 구문 분석한다
# selenium : 웹브라우저를 실행하고 제어한다. 서식을 채우고 마우스클릭을 시뮬레이션 한다

import webbrowser  # webbrowser open
import pyperclip   # 클립보드 복사
import requests    # 웹페이지 다운로드
import bs4         # html 페이지에서 정보를 추출하는 모듈

address = pyperclip.paste() # 주소입력 복사 www.naver.com
if address != None:
    # todo 정규식으로 인터넷 주소가 맞는지 확인
    webbrowser.open(address)

# clipboard 에서 복사한 주소로 구글 지도 열기
res = requests.get('https://finance.naver.com/')
if res.status_code == requests.codes.ok:
    print(res.text[:250]) # 250라인까지 출력

res = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status() # 오류가 있으면 에러를 던짐
play_file = open('./data/RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    play_file.write(chunk)

# html 에서 beautifulsoup 개체 만들기
res = requests.get('https://nostarch.com/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')

# html 파일 읽어오기
example_file = open('./data/example.html', )
example_soup = bs4.BeautifulSoup(example_file, 'html.parser')
#print(example_file)

elems = example_soup.select('#author')
len(elems)
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)

# 엘리먼트 속성에서 데이터 가져오기
spanElem = example_soup.select('span')[0]  # span 엘리먼트를 찾고 첫번째 속성
print(str(spanElem))
print(spanElem.get('id'))  # id 속성을 get에 전달하면 해당 속성값 author 를 돌려받는다
print(spanElem.attrs)