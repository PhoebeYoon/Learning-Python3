# 사칙연산
# 덧셈(+), 뺄샘(-), 곱셈(*), 나눗샘(/), 몫(//), 나머지(%), 제곱(**)


a = 10
b = 5
print(a+b) 
print(a-b) 
print(a*b) 
print(a/b) 
print(a//b) 
print(a%b) 
print(a**b) 


x = 100 # x에 100을 저장
x += 100    # x = x + 100
print(x) #200이 출력됨

y = 100
y //= y    # y = y / y
print(y) #1.0 (실수)

z = 3
z *= z   # z = z * z
print(z) # 9


m = 999
m -= m    # m = m - m
print(m) # 0


i=15
j=10
k = i%y  #5
i %=5  # i = i % 5 로 결과는 0


import math
print(math.ceil(5.1)) #올림 : 6
print(math.floor(3.874)) #내림 : 3

# 수학에서 사용되는 함수 중 절대값 표현
print(abs(-10)) #절대값 : 10

# 𝙼𝚊𝚝𝚑.𝚙𝚘𝚠
x =4
y=5
print(math.pow(x,y))  
print(math.pow(7, 2)); #49
print(math.pow(7, 3)); # 343
print(math.pow(2, 10)); # 1024

#제곱근 표현
print(math.sqrt( 9 ))

import random  
num=random.random()  
print("random 를 import 한 후",num) 
#random.randint() 함수는 제공된 숫자 범위에서 임의의 정수를 생성
num = random.randint(1, 500)  
print( "1~500 ", num )  
