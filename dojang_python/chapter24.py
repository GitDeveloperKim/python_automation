print('Hello world!'.replace('world', 'python'))
print(' '.join(['apple', 'grape', 'pineapple', 'orange'])) # 빈칸으로 띄어서 붙임 
print(','.join(['apple', 'grape', 'pineapple', 'orange'])) # , 컴마로 띄어서 붙임

# 양쪽의 특정 문자 삭제하기
print('., python ,,,,'.strip(',.'))

# 문자열 가운데 정렬
print('python'.center(10))

# 문자열 찾기
print('apple pineapple'.find('pl'))
