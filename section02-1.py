# Section02-1
# 파이썬 데이터 타입 종류 => Boolean, Numbers, String, Bytes, Lists, Tuples, Sets, Dictionaries

# 데이터 타입

v_str1 = "Nick"
v_bool = True
v_str2 = "Good"
v_float = 10.3
v_int = 1
v_dict = {
    "name": "Kim",
    "age": 13
}
v_tuple = 3, 4, 5, 2
v_set = {3, 4, 5, 5}
v_list = [2, 3, 4]

print(type(v_str1))
print(type(v_tuple))
print(type(v_list))
print(type(v_dict))
print(v_set)  # set은 중복제거


i1 = 38
i2 = 123
big_int1 = 12312313131231312321321312321343242421233
big_int2 = 3333333333334444444444444444444444444444444
f1 = 1.232
f2 = 2.4334
f3 = .5  # 0.5
f4 = 10.  # 10.0
print(i1*i2)
print(big_int2/big_int1)
print(big_int2//big_int1)  # 나눗셈(몫)
print(big_int2 % big_int1)  # 나눗셈(나머지)
print(f3+i1)  # 실수+정수 = 실수 => 자동형변환

result = f3 + i1
print(result, type(result))
