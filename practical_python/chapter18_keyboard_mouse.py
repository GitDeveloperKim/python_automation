import pyautogui

pyautogui.PAUSE = 1 # 함수호출은 작업을 수행한 후 1초를 기다린다
pyautogui.FAILSAFE = True

#해상도 사이즈 얻기
print(pyautogui.size())
width, height = pyautogui.size()

# 마우스 위치 얻기
mouse_x, mouse_y = pyautogui.position()
print(mouse_x, mouse_y)

# 마우스 움직이기
'''
for i in range(5):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
'''
# 현재 위치 기준으로 마우스 커서 옮기기
'''
for i in range(1):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
'''

# 스크롤 하기
#pyautogui.scroll(200)

# 컴퓨터 가상 키 입력 전송 -> 노트패드 열어서 마우스 클릭 후 타이핑?!
# pyautogui.typewrite('hello world!')
#pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y']) # 키보드 문자열 목록
# pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# 이미지 인식!!!!
#print(pyautogui.locateOnScreen('./data/start.png')) #
#pyautogui.click(4+3, 1032+3)

# 스크린샷 얻기
#im = pyautogui.screenshot()  # 테스트 결과 저장