## 모듈 ( Modules )
모듈이란 코드 라이브러리와 같다. 
응용프로그램에 포함할 기능들이 모아놓은 파일이라고 할 수 있다.
모듈을 만들려면 파일 확장자가 .py인 파일에 원하는 코드를 넣으면 된다


### 모듈을 만들어보자
파일이름은 mymodule.py
```python
def calling(name):
  print("Hello, " + name)
```
### 모듈을 사용할때는 
```python
import mymodule
mymodule.calling("Smith")
```
### 모듈은 array, dictionary, object를 포함할 수 있다

```python
#person.py 로 저장
person1 = {
  "name": "Smith",
  "age": 30,
  "country": "Korea"
}

```
```python
import person
a = mymodule.person1["age"]
print(a)
````

### 모듈에 별칭을 붙여 간단하게 사용하고자 한다면 'as' 키워드를 사용한다

```python
import person as pe
a = pe.person1["age"]
print(a)
```

### 이제 다른 예제로

``` python
# module1.py
# 클래스나 변수 등을 포함한 모듈

def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

터미널에서 실행한다
>>>python
>>>import module1
>>>print(module1.add(10,20))

>>>from module1 import sub
>>>sub(20,10)

>>>from module1 import *
>>>add (20,30)
50
>>> sub(30,4)
26
```

``` python
# module2.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

print(add(10,20))
print(sub(30,4))


>>python
>>import module2
30
26

위에서 import 만 했는데 print이 실행이 되었다
```

``` python
# module2.py를 아래와 같이 실행할 수도 있다
#def add(a, b):
#    return a + b

#def sub(a, b): 
#    return a-b
from module1 import *

print(add(10,20))
print(sub(30,4))

>>python
>>import module2
30
26

위에서 import 만 했는데 print이 실행이 되었다
```


