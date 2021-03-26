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

# 연산
print(c+d)

# 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)

# 리스트 함수
y = [5, 3, 2, 6, 7]
print(y)
y.append(9)  # 맨 끝에 9 추가
print(y)
y.sort()  # 오름차순 정렬
print(y)
y.reverse()  # 거꾸로 출력
print(y)
y.insert(2, 10)  # 2번 인덱스에 10 추가
print(y)
y.remove(2)  # 값 2 지우기
print(y)
y.pop()  # 맨 위의 값 꺼내서 없애기
print(y)
ex = [88, 77]
# y.append(ex) => 마지막에 list 형태로 들어가서 이중 list 형태
y.extend(ex)  # 현재의 list에서 연장하기
print(y)

# 삭제 : del, remove, pop

# Tuple (수정O, 중복O, 수정X, 삭제X)

# 선언
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])

print(c+d)
print(c*3)
print()

# 튜플 함수

z = (5, 3, 7, 2,3, 4)

print(z)
print(3 in z)
print(z.index(3)) # 3의 인덱스 값 반환
print(z.count(3))

