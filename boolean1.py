print(type(True))  
print(type(False))  
# print(false) 


int1 = 10
int2 = 200
float1 = .5
float2 = 10.
#형변환 int(정수), float(실수), complex(복소수)
print(int(float1)) #0
print(int(float2)) #10
print(float(int1)) #10.0
print(complex(3)) #(3+0j)
print(int(True)) #1
print(int(False)) #0
print(type(int(True))) #class 'int'
print(type(int(False))) #class 'int'
print(int('7')) # 7
print(complex(False)) #0j


# 진리값
print("참 : ", True)
print("거짓 : ", False)
print(1==1)
print(3>5)
print(3<5)
print(True or False)
print(True and False)
print(not False)
print(True==1)
print(False==0)
print(True + True)

# None

# 진리값
print("None : ", None)
print(None == 0)
print(None == [])
print(None == False)
print(None == "")
x = None
y = None
print(x == y)

# 아무값도 리턴하지 않는 함수
def void_function():
    a = 10
    b = 20
    c = a + b

result = void_function()
print(result)
print("값이없음" if result==None else result)