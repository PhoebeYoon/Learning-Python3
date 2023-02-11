## 데이터 타입
### 파이썬에는 6개의 테이터 타입이 있습니다.
1. Numeric Types: int(정수), float(소수), complex(복소수)
2. Sequence Types: str(문자열), list(리스트), tuple(튜플)
3. Mapping Type: dict(딕셔너리)
4. Set Types: set(집합)
5. Boolean Type: bool(불리언)
6. Binary Types: bytes, bytearray, memoryview

<img width="400" alt="스크린샷 2023-02-11 오후 9 20 01" src="https://user-images.githubusercontent.com/48478079/218257627-2875af77-1e42-4f2a-8fdc-c5e5691b6eaa.png">



```python
# Numeric Types : int / float / complex
# 1. int(정수형) : 소수점이 없는 정수
# 2. float(실수형) :  소수점이 있는 형태
# 3. complex(복소수) : 실수와 허수의 합인 복소수
# 수학적 기능을 사용하기 위해서는 import math 를 해야 함
num1 = 127  #1바이트로 표현할 수 있는 최대 양수
num2 = 0
num3 = -128 # #1바이트로 표현할 수 있는 최대 음수
print(num1, type(num1))
print(num2, type(num2))
print(num3, type(num3))

bin = 0b10  # 2진수 , 숫자0과 알파벳b
oct = 0o10  # 8진수 , 숫자0과 알파벳o
dec = 10    # 10진수
hex = 0x10  # 16진수 , 숫자0과 알파벳x
print(bin, type(bin))
print(oct, type(oct))
print(dec, type(dec))
print(hex, type(hex))

```
결과값을 확인하세요


```python
# 데이터 타입
v_str1 = "Superman" #str
v_str2 = "Wonderwoman" #str
v_bool = True #boolean 
v_float = 10.1 #float
v_int = 3 #int
v_complex = 3 + 3j #complex number
v_dict = {
    "name" : "Hong",
    "age" : 24,
    "city" : "Seoul"
} #dictinary
v_list = [3,5,7] #list
v_tuple = 3,5,7 #tuple
v_set = {7,8,9} #set

print(type(v_str1)) # <class 'str'>
print(type(v_str2)) # <class 'str'>
print(type(v_bool)) # <class 'bool'>
print(type(v_float)) # <class 'float'>
print(type(v_int)) # <class 'int'>
print(type(v_complex)) # <class 'complex'>
print(type(v_dict)) # <class 'dict'> 
print(type(v_list)) # <class 'list'>
print(type(v_tuple)) # <class 'tuple'>
print(type(v_set)) # <class 'set'>
```

