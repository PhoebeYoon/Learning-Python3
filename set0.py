Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    
    
    
# Set() 명령을 이용하여 집합을 만들자
Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i) 


# 정수, 플로트, 튜플 등과 같은 모든 유형의 요소를 포함할 수 있습니다. 
set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
print('type(set1) ',type(set1))  

# 그러나 가변 요소(목록, 사전, 집합)는 집합의 구성원이 될 수 없습니다.
set2 = {1,2,3,["Javatpoint",4]}  
print('type(set2) ',type(set2))   