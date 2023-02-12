## 데이터 타입
### 파이썬에는 6개의 테이터 타입이 있습니다.
1. Numeric Types: int(정수), float(소수), complex(복소수)
2. Sequence Types: str(문자열), list(리스트), tuple(튜플)
3. Mapping Type: dict(딕셔너리)
4. Set Types: set(집합)
5. Boolean Type: bool(불리언)
6. Binary Types: bytes, bytearray, memoryview

<img width="450" height="340" alt="스크린샷 2023-02-11 오후 9 20 01" src="https://user-images.githubusercontent.com/48478079/218264409-d45482c2-d7e0-4d99-a261-3a5631f05591.png">


### 1. Numeric Types: int(정수), float(소수), complex(복소수)

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


### 2. Sequence Types: str(문자열), list(리스트), tuple(튜플)
- 문자열
```python
# 1. 문자열(string) : 문자, 단어로 이루어진 문자들의 집합
# 2. 추가,삭제, 수정, 길이 구하기, 인덱싱, 슬라이싱, 위치찾기, 갯수구하기 등 


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

- 리스트
1. [   ] 기호를 사용한다
2. indexing, slicing , pop(), del(), remove(), count(), sort(), reverse(),append(), extend() 등
  
``` python
# 리스트 생성
List = []  
print("JavaTpoint data List: ")  
print(List)  
     
# 숫자가 들어간 리스트
List1 = [12, 24, 64, 18, 3, 201, 65, 35, 27, 29, 58, 42, 87, 30, 28, 79, 4, 90]  
print("\n List of numbers: ")  
print(List1)  
     
# 인덱스를 이용하여 요소를 추출
List2 = ["let's", "learn", "Python", "from", "JavaTpoint"]  
print("\nList Items: ")  
print(List2[0])   
print(List2[2])  
print(List2[1])  
print(List2[4])  
print(List2[3]) 

```

  
- 튜플 (tuple1.py 참조 )   
1. 리스트와 매우 유사하지만, 우선 리스트는 [ ] 기호를 튜플은 (  ) 기호를 사용한다
2. 리스트는 생성,수정, 삭제가 가능하지만 튜플은 값을 바꿀 수 없다. 
3. 튜플이 1개의 값만 갖는다면 값 뒤에 콤마(,) 삽입해야 하고 ( ) 는 생략가능하다
4. 리스트처럼 슬라이싱, 길이구하기 등 기본적인 것은 리스트와 동일하다

> 튜플은 여러개의 변수에 여러개의 값을 한 문장으로 할당할 수 있다   
> 튜플은 데이터가 변경되지 않는 구조이기 때문에 튜플의 정렬에 대해서는(tuple2.py 참조 )

### 3. 딕셔너리 (Dictionary )
1. key 와 value 쌍으로 되어 있다 (  key : value )
2. 요소를 접근할 때 key 를 통해 접근한다
3. {   } 로 둘러싸여있고 추가, 삭제, 수정 등이 가능하다


### 4. Set (집합)
1. 집합은 set 키워드를 사용하며 중괄호 {   } 사이에 정의된다
2. 집합의 각 요소는 고유하고 불변해야 하며 중복요소를 가지면 안됩니다. 
3. 집합은 변형 변형가능하므로 생성 후에 수정이 가능합니다
4. set은 정렬되지 않는 항목 또는 데이터 유형의 모음으로 저장된 요소의 순서가 고정되어 있지 않아서 인덱스를 이용한 접근이 불가능하다
5. int, float, tuple 유형의 요소를 포함할 수 있지만 가변요소 ( 리스트, 딕셔너리, 집합) 은 집합의 요소가 될 수 없습니다 
6. 교집합, 합집합, 차집합을 구하는데 용이합니다 

``` python
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)   

```
``` python
set5 = {1,2,4,4,5,8,9,9,10}  
print("Return set with unique elements:",set5)   # 중복된 요소를 제거합니다
```


> 리스트 vs 집합 비교
``` python
List1 = [9, 3, 6, 19, 67, "Hey", "JavaTpoint", 78, 2, 1]  
List2 = [9, 3, 6, 19, 67, 78, "Hey", "JavaTpoint", 2, 1]  
print("List1 = ", List1)  
print("List2 = ", List2)  
print('List1 == List2 ? ', List1 == List2) # 결과는 False


setB= set(["let's", "learn", "Python", "from", "JavaTpoint",10]) 
setC= set(["learn","let's",  "Python", 10,"JavaTpoint", "from"]) 
print('SetB == SetC ? ', setB == setC) # 결과는 True
 
```

### 5. Boolean 
1. 불리언 형은 True, False 로 나타내는 자료형으로 2가지 값만 가집니다
2. 빈자료형  { } , [ ], ( ), " "  모두 숫자 0 으로 None은 False, 나머지는 True


