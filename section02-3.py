# Section 02-3
# 파이썬 데이터 타입(자료형)
# List, Tuple

# List(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Orange']  # 데이터 타입이 달라도 가능
e = [10, 100, ['Pen', 'Orange']]

# Index
print(d[2])  # Pen
print(d[-2])  # Pen
print(d[0]+d[1])
print(e[2][0])  # Pen
print(e[-1][-2])  # Pen

# Slicing
print(d[0:3])  # [10, 100, 'Pen']
print(e[2][0:2])  # ['Pen', 'Orange]'
