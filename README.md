## 모듈 ( Module )
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

```python
# module3.py
#클래스나 변수 등을 포함한 모듈
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 

```

