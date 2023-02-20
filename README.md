
### 클래스의 상속에 대해 알아보자

``` python

class Employee:
    interest = 1.02
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay =pay
        
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def sallay(self):
        self.pay = int(self.pay * self.interest)
        return self.pay
             

class Developer(Employee):
    interest = 1.10
    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self,first,last,pay) 이렇게 대치해서 사용되도 된다
        self.prog_lang = prog_lang
    

class Manager(Employee):
    def __init__(self, first, last,pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:

            self.employees.remove(emp)
            
            
    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())
            


em1 = Employee('Kim', 'Smith' ,5000)
em2 = Developer('Lee', 'John' ,6000,'java')
em3 = Developer('Park', 'Porter' ,5000,'Python')
#man1= Manager("Ru",'Jane', 9000, [em1]) 
man1= Manager("Ru",'Jane', 9000) # 매니저 부분을 empty로 지정하면 아무것도 나오지 않는다  A)

print(em1.fullname())
print(em2.fullname())
print(em3.fullname())
print(man1.fullname())

print(em1.sallay())
print(em2.sallay())
print(em3.sallay())
print(man1.sallay())


man1.print_emps() #매니저를 지정하지 않으면 아무것도 출력되지 않는다.  A)
man1.add_emp(em2) # 그래서 add_emp(em2) 로 하면 클래스내의 employees=[] 에 em2 가 저장되어
man1.print_emps() # 여기서 --> Lee John 으로 나온다

# 매니저가 em2 로 등록되어 있지만 em1를 추가해 보자
man1.add_emp(em1)
print(" ** 매니저 리스트 ** ")
man1.print_emps() 

print("** 매니저 삭제 **")
man1.remove_emp(em2)
man1.print_emps() 

print(" * is sub class ? ") 
# issubclass(자식클래서, 부모클래스) 클래스 상식관계를 알아보는 것으로 기본적으로 빌트인 모듈이라
# 따로 import 할 필요없다
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))
```
