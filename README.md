## 조건문 if 문에 대해 알아봅니다
### if 문에는 조건이 온다 그리고 elif는 if문이 참일 아닐때 실행, else은 if문이든 elif문이든 해당되지 않을때 실행된다고 보면 된다

```python
a = 33
b = 200

if b > a:
  print("b is greater than a")

```
### if ~ elif 
```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
```


### if ~ elif ~ else
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

```

### if문을 한줄로 사용
```python
a = 200
b = 33
if a > b: print("a is greater than b")
```
### and문
```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

```

### or문
```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
```


```python
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
```

### if문안에 if문
```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

```
### pass 사용
```python
a = 33
b = 200

if b > a:
  pass
```

