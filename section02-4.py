# Section02-4
# 파이썬 데이터 타입(자료형)
# Dictionary, Set

# Dictionary : 순서 X, 중복 X, 수정 O, 삭제 O

# key, value 형태
# 선언

a = {'name': 'Kim', 'Phone': '010-0000-0000', 'Birth': 970315}
b = {0: 'Hello, Python', 1: 'Hello, Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('name'))
print(a.get('address'))  # None 출력
print(c['arr'][1:3])

# 추가
a['Adress'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank1'] = (1, 2, 3)
print(a)

# keys, values, items
print(a.keys())  # key 출력
print(list(a.keys()))  # list 형태로 key 출력

temp = list(a.keys())
print(temp[1:3])

print(a.values())  # value 출력
print(list(a.values()))

print(a.items())  # key,value 쌍으로 출력
print(list(a.items()))

# Set
