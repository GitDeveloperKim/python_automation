# dictionary
# 연습문제 12.4
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])

# 심사문제 12.5
keys = input().split()
values = map(float, input().split()) #input().split()는 문자열로 받아오기때문에 map으로 float 변환
print(dict(zip(keys, values))) #zip 을 이용해서 list 두개를 합치면 된다