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

#문자열 연산
str_o1 = '*'
str_o2 = 'abd'
str_o3 = 'ded'

print(str_o2 * 100) # 반복
print(str_o2 + str_o3)
print( 'd' in str_o3) # 해당 문자가 포함되어 있는지
print( 'd' not in str_o3) # 해당 문자가 포함되어 있지 않는지