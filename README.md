
## 모듈에 대해 더 알아봅시다

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

터미널로 이동하여 >python 엔터 
>>> dir() # 1번 결과확인
>>> from pkg import * 
>>> dir() # 2번 결과확인
# 결과를 확인해 보면 2번은 1번과 달리 mod1.py ~ mod4.py가 포함된 것을 확인할 수 있다   
<img width="346" alt="스크린샷 2023-02-19 오후 12 05 07" src="https://user-images.githubusercontent.com/48478079/219910345-887c6de2-5dd3-4528-a595-6824de5b97e4.png">
