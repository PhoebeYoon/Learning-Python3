# set에서 해당 숫자 제거하기
my_set = {1,2,3,4,5,6,12,24}  
n = int(input("Enter the number you want to remove"))  
my_set.discard(n)  
print("After Removing:",my_set)  

#Write a program to add multiple elements to the set.
set1 = set([1,2,4,"John","CS"])  
set1.update(["Apple","Mango","Grapes"])  
print(set1)  

# Write a program to find the union between two set.

set1 = set(["Peter","Joseph", 65,59,96])  
set2  = set(["Peter",1,2,"Joseph"])  
set3 = set1.union(set2)  
print(set3)

# Write a program to find the intersection between two sets.
set1 = {23,44,56,67,90,45,"Javatpoint"}  
set2 = {13,23,56,76,"Sachin"}  
set3 = set1.intersection(set2)  
print(set3)  

#Write the program to add element to the frozenset.
print(" frozenset ")
set1 = {23,44,56,67,90,45,"Javatpoint"}  
set2 = {13,23,56,76,"Sachin"}  
set3 = set1.intersection(set2)  
print(set3) 

#세트는 부분집합, 진부분집합, 상위집합, 진상위집합과 같이 속하는 관계를 표현할 수도 있습니다. 현재 세트가 다른 세트의 (진)부분집합 또는 (진)상위집합인지 확인할 때는 세트 자료형에 부등호와 등호 사용합니다.
print('----------------------')
set1 = set(["Peter","James","Camroon","Ricky","Donald"])  
set2 = set(["Camroon","Washington","Peter"])  
set3 = set(["Peter"])  
  
issubset = set1 >= set2  
print(issubset)  #fasle , 왼쪽집합이 오른쪽 집합의 상위집합인지 확인 = 가 있으므로 같을 때도 참

issuperset = set1 <= set2  
print(issuperset)  # false,왼쪽에 있는 집합이 오른쪽집합의 부분집합인지 확인, = 가 있으므로 같을 때도 참

issubset = set3 <= set2  
print(issubset)   #true 

issuperset = set2 >= set3  
print(issuperset) # true

print(" 세트가 같은지 다른지 비교하기")
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})
print(a == {1, 2, 4, 3 })

print("세트에 겹치는 요소가 있는 지 없는지 확인하기")
print(a.isdisjoint({5, 6, 7, 8})  ) # True
print(a.isdisjoint({3, 4, 5, 8})  ) # False