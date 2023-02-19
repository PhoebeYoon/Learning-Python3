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


### 간단한 계산 프로그램 만들기

```python
class Calculator:
    def plus(self, x, y):
        return x+y
    def minus(self, x, y):
        return x-y
    def multiply(self, x, y):
        return x*y
    def divide(self, x, y):
        return x/y

calc = Calculator()
print(calc.plus(1, 2))
print(calc.minus(1, 2))
print(calc.multiply(1, 2))
print(calc.divide(1, 2))

```
또 다르게 만들어보면,

``` python
class Calculator:
    def plus(self, x, y):
        return x+y
    def minus(self, x, y):
        return x-y
    def multiply(self, x, y):
        return x*y
    def divide(self, x, y):
        return x/y

calc = Calculator()
num1  = int(input("첫번째 입력>>"))
num2  = int(input("두번째 입력>>"))
dowhat = input(" + - *  / 중 1개만 선택하세요")
dowhat = dowhat.strip() # 공백이 있을 수 있으니 제거한다
# 공백제거를 위해 dowhat = dowhat.replace(" ","") replace 문을 사용할 수도 있다
if dowhat =="+": print(calc.plus(num1, num2))
if dowhat =="-": print(calc.minus(num1, num2))
if dowhat =="*": print(calc.multiply(num1, num2))
if dowhat =="/": print(calc.divide(num1, num2))
# 파이썬에는 switch ~ case 문이 없기 때문에 if 문으로 
```
