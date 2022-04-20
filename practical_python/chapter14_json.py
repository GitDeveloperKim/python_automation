import json
'''
웹 사이트와 상호작용할 수 있는 방법 
JSON은 애플리케이션 프로그래밍 인터페이스를 제공 
공공기관의 데이터를 가져오거나 보낸다 
'''

# json dumps() 이용하기 : dump strings
dict_data = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
json_data = json.dumps(dict_data)
print(json_data)

#