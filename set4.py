#Union of two Sets

# using union | operator
days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
days2 = {"Friday","Saturday","Sunday"}    

print('Days1|Days2',days1|days2) #printing the union of the sets     
print('Days1.union(Days2)',days1.union(days2)) #printing the union of the sets   


#Intersection of two sets
# Using & operator
days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(days1 & days2) #prints the intersection of the two sets    
# Using intersection() method
set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2))
set1 = {1,2,3,4,5,6,7}  
set2 = {1,2,20,32,5,9}  
set3 = set1.intersection(set2)  
print(set3)  


#intersection_update() 메서드는 원하지 않는 항목을 제거하여 원래 집합을 수정하지만 intersection() 메서드는 새 집합을 반환하므로 intersection() 메서드와 다릅니다.
#intersection_update() 메서드는 다른 두 집합 모두에 없는 요소를 a집합에서 제거하여 원래 a집합의 내용을 수정합니다
a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway","bob"}    
c = {"fuson", "gaurav", "castle"}    
    
a.intersection_update(b, c)    
    
print('intersection_update 후 a',a)  
print('intersection_update 후 b',b) 
print('intersection_update 후 c',c) 



# Difference between the two sets
# Using subtraction ( - ) operator
days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
days2 = {"Monday", "Tuesday", "Sunday"}    
print(days1-days2) #{"Wednesday", "Thursday" will be printed}  
#Using difference() method
print(days1.difference(days2)) # prints the difference of the two sets Days1 and Days2   


#Difference of two sets ( 두집합에서 중복된 부분을 제외하고 나머지들)
# Using ^ operator

a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a^b  
print(c)  
d = a.symmetric_difference(b)  
print(d)


# 비교 < , > , <= , >=
#Python을 사용하면 비교 연산자, 즉 <, >, <=, >=를 세트와 함께 사용할 수 있으며, 이를 통해 세트가 서브셋인지, 슈퍼셋인지 또는 다른 세트와 동등한지 확인할 수 있다. 집합 내부에 있는 항목에 따라 true 또는 false 부울 값이 반환됩니다
days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
days2 = {"Monday", "Tuesday"}    
days3 = {"Monday", "Tuesday", "Friday"}   
#Days1 is the superset of Days2 hence it will print true.     
print ('days1>days2 ',days1>days2)    
print('days1.issuperset(days2) : ',days1.issuperset(days2))


#prints false since Days1 is not the subset of Days2     
print ('days1<days2 ',days1<days2)    
print('days1.issubset(days2)   : ',days1.issubset(days2))
print('days2.issubset(days1)   : ',days2.issubset(days1))   
    
    
#prints false since Days2 and Days3 are not equivalent     
print ('days2 == days3 ',days2 == days3)    

#고정 집합은 일반 집합의 불변 형태이다. 즉, 고정 집합의 항목은 변경할 수 없으므로 사전에서 키로 사용할 수 있다

Frozenset = frozenset([1,2,3,4,5])     
print(type(Frozenset))    
print("\nprinting the content of frozen set...")    
for i in Frozenset:    
    print(i);    
#Frozenset.add(6) 
#gives an error since we cannot change the content of Frozenset after creation 

# frozenset 를 이용한 딕셔너리
dict = {"Name":"John", "Country":"USA", "ID":101}     
print(type(dict))    

Fset = frozenset(dict); #Frozenset will contain the keys of the dictionary    
print(type(Fset))    
for i in Fset:     
    print(i)  
# 출력결과시에 name, country, id 의 순서가 실행시마다 바뀐다
