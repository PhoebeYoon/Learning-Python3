## 모듈에 ㅡㅡallㅡㅡ 사용하기

'module' 브랜치에서 <b>form '모듈' import * </b>할때는 모듈의 모든 내용을 가져와서 사용하는데 문제가 없다 그러나 이것을 패키지에 사용할때는 (<b>from 패키지 import * </b> )문제가 발생한다. 

### 실습을 해보자
<pre>
\pkg
    \sub_a
        __init__.py
        mod1.py
        mod2.py
    \sub_b 
        __init__.py
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



### 모듈을 만들어보자

```python

```
