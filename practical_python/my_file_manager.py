import os

def fileOpen():
    f = open('input.txt','r')
    return f

if __name__ == '__main__':
    # 현재 경로 얻어오기 getcwd
    current_path = os.getcwd()
    print(current_path)
    print(os.path.abspath(current_path))

    # 폴더 만들기
    if os.path.exists(r'C:\Users\default.DESKTOP-9K8MUSK\Documents\dev') \
            and not os.path.exists(r"C:\Users\default.DESKTOP-9K8MUSK\Documents\dev\test_workspace"):
        os.makedirs(r"C:\Users\default.DESKTOP-9K8MUSK\Documents\dev\test_workspace")

    # join
    print(os.path.join('usr', 'bin', 'spam'))

    # 분해하기
    print(current_path.split(os.path.sep))

    # 파일 open
    f = fileOpen()
    print(f.readline())
    f.close()