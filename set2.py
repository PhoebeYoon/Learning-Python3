# set의 기본 형태 : 리스트형태나 문자열 형태로 만들 수 있음
s1 = set([1,2,3,1,2,3])
s2 = set("Hello")
print(s1) # {1,2,3}
print(s2) # {'l', 'o', 'e', 'H'} -> 중복이 제거됨


# 집합에서 인덱싱을 할 수 없기 때문에 요소값을 추출하려면 리스트나 튜플로 변환시킨 후 제어함
list_s1 = list(s1) # 리스트 변환
list_s2 = list(s2) # 리스트 변환
print(list_s1) # [1, 2, 3]
print(list_s2) # ['e', 'o', 'H', 'l']
print(list_s1[1]) # 2
print(list_s2[1]) # H -> 계속 값이 바뀜,, 리스트로 바뀌는 과정에서 순서가 랜덤으로 위치함
# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 교집합 : 교집합은 집간 간 공통으로 있는 요소를 추출함
print(s1&s2) # {4, 5, 6}
print(s1.intersection(s2)) # {4, 5, 6}
# 합집합 : 중복없이 집간 간 요소들을 모두 합침
print(s1|s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 차집합 : 집합 간의 뺄셈
print(s1-s2) # {1, 2, 3}
print(s1.difference(s2)) # {1, 2, 3}
# 집합 관련된 함수들
# 값 1개 추가하기(add) : 1개만 가능
s1 = set([1,2,3])
s1.add(4)
print(s1) # {1, 2, 3, 4}
# 값 여러개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1) # {1, 2, 3, 4, 5, 6}
# 특정 값 제거(remove)
s1 = set([1,2,3])
s1.remove(3)
print(s1) # {1, 2}
#  set 활용 : 중복없음, 집합 연산
data1 = {"apple", "samsung", "lg"}
data2 = {"samsung", "lg", "MS"}
print(data1&data2) # {'lg', 'samsung'} -> 교집합
print(data1|data2) # {'lg', 'MS', 'apple', 'samsung'} ->합집합
print(data1-data2) # {'apple'} -> 차집합
print(data1^data2) # {'MS', 'apple'} -> 합집합-교집합
#중복 없애기
data_list = ["apple", "samsung", "lg", "samsung", "lg", "MS", "dell", "HP", "dell", "HP", "samsung"]
# {'dell', 'samsung', 'MS', 'lg', 'HP', 'apple'}