import os, shutil

def file_open():
    file = open('data/input.txt', 'r')
    return file

def use_shutil():
    if os.path.exists(r'C:\Users\default.DESKTOP-9K8MUSK\Documents\dev\test_workspace\eggs.txt'):
        shutil.move(r'C:\Users\default.DESKTOP-9K8MUSK\Documents\dev\test_workspace\eggs.txt', r"C:\Users\default.DESKTOP-9K8MUSK\PycharmProjects\python_automation\practical_python\bacon.txt")

def use_os_walk():
    for folderName, subFolders, fileNames in os.walk(os.getcwd()):
        print('current folder is '+folderName)

        for subFolder in subFolders:
            print('SubFolder of '+folderName+':'+subFolder)

        for fileName in fileNames:
            print('File inside'+folderName+':'+fileName)

        print('\n')

def moveAnotherFileName():
    #date pattern
    src = os.path.join(os.getcwd(), 'bacon.txt')
    dst = os.path.join(os.getcwd(), 'date.txt')
    moveFile(src, dst)

def moveFile(src, dst):
    if os.path.exists(src):
        shutil.move(src, dst)

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

    #shutil 사용해보기
    use_shutil()

    #use os walk()
    use_os_walk()

    #move file name
    moveAnotherFileName()

    # 파일 open
    f = file_open()
    print(f.readline())
    f.close()