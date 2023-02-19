## 모듈에 ㅡㅡallㅡㅡ 사용하기

'module' 브랜치에서 <b>form '모듈' import * </b>할때는 모듈의 모든 내용을 가져와서 사용하는데 문제가 없다 그러나 이것을 패키지에 사용할때는 (<b>from 패키지 import * </b> )문제가 발생한다. 

### 실습을 해보자
<pre>
\pkg
        __init__.py
        mod1.py
        mod2.py
        mod3.py
        mod4.py
</pre>

```python
# mod1.py
def foo():
    print('[mod1] foo()')

class Foo:
    pass

```
```python
# mod2.py
def bar():
    print('[mod2] bar()')

class Bar:
    pass
```


```python
# mod3.py
def baz():
    print('[mod3] baz()')

class Baz:
    pass
```

```python
# mod4.py
def qux():
    print('[mod4] qux()')

class Qux:
    pass

```
ㅡㅡinitㅡㅡ.py 는 빈파일로 한다   

이제 터미널에서 다음을 실행해보자
```
>>> python
>>> from pkg import *
>>> mod1.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'mod1' is not defined
```
라고 출력된다
이제  ㅡㅡinitㅡㅡ.py 의 내용에 아래의 내용을 추가해 본다
```python
__all__ = [
        'mod1',
        'mod2',
        'mod3',
        'mod4'
        ]

```

<pre>
>>> python
>>> from pkg import *
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'mod1', 'mod2', 'mod3', 'mod4']
>>> mod1.foo()
[mod1] foo()
</pre>

여기서 <b>from 패키지 import * </b>는 모든것을 불러오겠다는 것인데, 그 '모든 것'이 뭔지를 모르는 것이다.   
그래서 ㅡㅡallㅡㅡ = [  ] 로 모든것이 뭔지를 지정해 주는 것이다.  

### 그럼, 여기서 ㅡㅡnameㅡㅡ 이 뭔지를 알아보자  
파이썬파일에는 <b> ㅡㅡnameㅡㅡ </b> 라는 변수가 이다. 이 변수는 모듈의 이름을 가지고 있다.  
위에서 했던 예에서 ㅡㅡinitㅡㅡ.py 의 내용을 바꿔보자

```python
#__init__.py 에 내용을 변경
print(f'초기화파일불러오기{__name__}')
A =['mod1','mod2','mod3','mod4']
```


