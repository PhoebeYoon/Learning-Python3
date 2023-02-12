# 집합의 데이타 구조는 이렇게 생겼습니다 
# First, we will create the Set  
setA = set()  
print("Intial JavaTpoint Set: ")  
print(setA)  
     
# we are creating the Set by using Constructor  
# we will use object for Storing String) 
String = 'lets learn Python from JavaTpoint'  
setA = set(String)  
print("\n 저장된 형태: " )  
print(setA)  
     
# now, we will create the Set by using the list  
setB= set(["let's", "learn", "Python", "from", "JavaTpoint"])  
print("\n List를 이용한 집합: ")  
print(setB)  
#여러번 실행시켜 결과가 동일하게 출력되지 않다는 것을 확인한다