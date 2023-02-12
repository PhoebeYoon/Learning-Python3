#Using add() method
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nAdding other months to the set...");    
months.add("July");    
months.add ("August");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)    
    
#  Using update() method
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nupdating the original set ... ")    
months.update(["July","August","September","October"]);    
print("\nprinting the modified set ... ")     
print(months)

# Using discard() method
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.discard("January");    
months.discard("May");    
print("\nPrinting the modified set...");    
print(months)    
print("\nlooping through the set elements ... ")    
for i in months:    
    print(i)  
# Using remove() method
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.remove("January");    
months.remove("May");    
print("\nPrinting the modified set...");    
print(months)    
# pop() 는 보통 마지막 요소를 제거합니다
months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(months)    
print("\nRemoving some months from the set...");    
months.pop();    
months.pop();    
print("\nPrinting the modified set...");    
print(months)  


# Python provides the clear() method to remove all the items from the set.
Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving all the items from the set...");    
Months.clear()    
print("\nPrinting the modified set...")    
print(Months)   

# remove() 와 discard() 의 차이점
# discard()를 사용하여 집합에서 삭제할 키가 집합에 없으면 Python은 오류를 제공하지 않습니다. 프로그램은 제어 흐름을 유지합니다.

# 반면, remove()를 사용하여 세트에서 삭제할 항목이 세트에 존재하지 않으면 Python에서 오류가 발생합니다

Months = set(["January","February", "March", "April", "May", "June"])    
print("\nprinting the original set ... ")    
print(Months)    
print("\nRemoving items through discard() method...");    
Months.discard("Feb"); #will not give an error although the key feb is not available in the set    
print("\nprinting the modified set...")    
print(Months)    
print("\nRemoving items through remove() method...");    
Months.remove("Jan") #will give an error as the key jan is not available in the set.     
print("\nPrinting the modified set...")    
print(Months)    