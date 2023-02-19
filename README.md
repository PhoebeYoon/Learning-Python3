
## 모듈에 대해 더 알아봅시다
#### 패키지를 만들때 ㅡㅡinitㅡㅡ.py 라는 이름의 파일이 있으면 패키지 초기화 코드의 실행에 사용할 수 있다



1. pkg폴더를 만들고 mod1.py, mod2.py, mod3.py, mod4.py 그리고 __init__.py 이렇게 5개의 파일을 만든다
```python
#mod1.py
def foo():
    print('[mod1] foo()')

class Foo:
    pass
```
```python
#mod2.py
def bar():
    print('[mod2] bar()')

class Bar:
    pass
```
```python
#mod3.py
def baz():
    print('[mod3] baz()')

class Baz:
    pass
```
```python
#mod4.py
def qux():
    print('[mod4] qux()')

class Qux:
    pass
```
```python
#__init__.py
__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]

```

터미널로 이동하여  
python 엔터  > dir() # 1번 결과확인  > from pkg import *  >  dir() # 2번 결과확인   
결과를 확인해 보면 2번은 1번과 달리 mod1.py ~ mod4.py가 포함된 것을 확인할 수 있다    

<img width="746" alt="스크린샷 2023-02-19 오후 12 05 07" src="https://user-images.githubusercontent.com/48478079/219910345-887c6de2-5dd3-4528-a595-6824de5b97e4.png">    
 
터미널에서 >>> from pkg.mod3 import *   
터미널에서 >>> baz()   # 결과로 [mod3] baz() 가 출력된다


### 이제 서브패키지를 만들어보자
<pre>
\pkg
    \sub1  
        ㅡㅡinitㅡㅡ.py  
        mod1.py  
        mod2.py  
    \sub2    
        ㅡㅡinitㅡㅡ.py  
        mod3.py  
        mod4.py  
</pre>   

위에서 만들었던 파일을 재사용하고 ㅡㅡinitㅡㅡ.py는 빈파일로 만든다   

터미널로 이동 후,  

<img width="530" alt="스크린샷 2023-02-19 오후 1 00 51" src="https://user-images.githubusercontent.com/48478079/219921434-b9e5dc93-bcbc-4da1-8c52-1b69302344f1.png">   
sub2 패키지를 불러오고 나서 sub1 패키지에 있는 foo() 를 부른것이다. 당연히 에러가 발생한다   

이제 mod3.py 의 내용을 바꾼다
```python
def baz():
    print('[mod3] baz()')

class Baz:
    pass

from pkg.sub1.mod1 import foo
foo()
```   
변경후에, 
```
>>> from pkg.sub2  import mod3
[mod1] foo()
>>> mod3.foo()
[mod1] foo()
```
