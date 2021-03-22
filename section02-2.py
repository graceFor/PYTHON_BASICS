# Section02-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am girl"
str2 = "HyunKyung"
str3 = ''
str4 = str()  # 공백
str5 = str('ace')

print(len(str1), len(str2), len(str3))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'/Users/hyunkyung/Desktop/python_basics'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# Multi Line => \ = escape
multi = \
    """ 
문자열

멀티라인 
테스트 
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abd'
str_o3 = 'ded'

print(str_o2 * 100)  # 반복
print(str_o2 + str_o3)
print('d' in str_o3)  # 해당 문자가 포함되어 있는지
print('d' not in str_o3)  # 해당 문자가 포함되어 있지 않는지

# 문자열 함수

a = 'nice'
b = 'orange'

print(a.islower())  # 문자열이 다 소문자인가
print(a.endswith('s'))  # 문자열의 끝이 's'로 끝나는가
print(a.capitalize())  # 문자열의 첫 글자만 대문자로 변환
print(a.replace('nice', 'good'))  # nice를 good으로 변환
print(list(reversed(b)))  # b 문자열을 거꾸로 한글자씩 list 형태로 변환

# slice

c = 'abcdef'
d = 'ghjwe'

print(c[0:3])  # 0부터 2까지(3 전까지)
print(c[0:])  # 전체
print(c[0:len(c)])  # 전체
print(d[0:4:2])  # 0~3까진데 2개씩 건너뛰어서 출력
print(d[1:-2])
print(d[::-1])  # 처음부터 끝까지 나오는데 역순으로 출력
