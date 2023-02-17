
## 클래스에서 __init__ 사용과 setdata() 사용 예

``` python
# setdata() 사용 예
class FourCal:
    def setdata(self, first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
#print(a)

a.setdata(4,2)
b.setdata(3,8)

print(a.add())
print(b.add())

```


``` python
#__init__ 사용 예
class FourCal:
    def __init__(self,first,second):
         self.first = first
         self.second = second
         
    def add(self):
        return self.first + self.second
    
    def sub(self):
        return self.first - self.second
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second
    
    

a = FourCal(4,2)
b = FourCal(3,8)

print(a.add())
print(b.add())
```
