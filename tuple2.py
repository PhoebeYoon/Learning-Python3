# 튜플은 데이터가 변경되지 않는 구조이기 때문에 
#sorted(tuple, sort_fun)으로 튜플을 정렬할 수 있다


# 방법1. 정렬에 대한 규칙을 만들어서 정렬해야 하며 리턴되는 결과를 다시 튜플로 만들어야 한다 

def sort_num(x):
    return x

numbers = (10, 3, 11, 9, 8)
sorted_number = tuple(sorted(numbers, key=sort_num))
print(sorted_number)

# 방법2. labmda 표현식을 이용
numbers = (10, 3, 11, 9, 8)
sorted_number = tuple(sorted(numbers, key=lambda x: x))
print(sorted_number)

# int 과 스트링이 섞여있는 구조일때
numbers = (10, '3', 11, 9, '8')
sorted_number = tuple(sorted(numbers, key=lambda x: int(x)))
print(sorted_number)