# 딕셔너리 기본 형태
dict1 = {"name":"jawon", "age":20, "phone":"010-1111-2222"}
dict2 = {1:"hi"}
dict3 = {"a":[1,2,3]}
dict4 = {}


# 딕셔너리 쌍 추가하기 : 리스트 추가와 유사하나 []안에 키값을 넣음
dict1 = {1:'a'}
dict1[2] = "b" # 추가
print(dict1) # {1: 'a', 2: 'b'}
dict1["name"] = "jaewon"  # 추가
dict1["age"] = 20 # 추가
print(dict1) # {1: 'a', 2: 'b', 'name': 'jaewon', 'age': 20}
dict1[3] = [1,2,3,4]
print(dict1) # {1: 'a', 2: 'b', 'name': 'jaewon', 'age': 20, 3: [1, 2, 3, 4]}


# 딕셔너리 요소 삭제하기(del) : del dictName[key값] 으로 지울 수 있고, key:value쌍이 지워짐
dict2 = {"name":"jaewon", "age":"20", "location":"seoul", 1:"a", "list_a":[1,2,3,4,5]}
del dict2["list_a"]
print(dict2) # {'name': 'jaewon', 'age': '20', 'location': 'seoul', 1: 'a'}
del dict2[1]
print(dict2) # {'name': 'jaewon', 'age': '20', 'location': 'seoul'}


# 딕셔너리에서 value값 얻기
# 리스트, 튜플, 문자열은 요솟값을 얻고자 할 때 인덱싱이나 슬라이싱 기법을 사용하였으나,
# 딕셔너리에서는 key를 사용해 value를 구하는 방법을 사용함
# 왜냐하면 딕셔너리에는 index 순서가 없고, key으로 index 하기때문
a = {1:"a", 2:"b", "name":"jaewon", "age":20, "a":[1,2,3,4,5]}
print(a[1]) # a
print(a["name"]) # jaewon
print(a["age"]) # 20
print(a["a"]) # [1,2,3,4,5]


# get을 통해 value값 가져오기 -> 위 처럼 key를 통해 value를 호출할 수 있으나, 없는 key를 호출하면 오류가 발생함
# get을 통해 value를 가져올 때 존재하지 않는 key를 이용하면 None를 돌려줌
print("---------------")
a = {'name':'smith', 'phone':'01012345678', 'birth': '1990'}
print(a["name"]) # smith
print(a.get("name")) # smith
# print(a["location"]) # 오류발생
print(a.get("location")) # None 반환
print(a.get("location", "value is not")) # value is not 반환 -> 두번째에 미리 디폴트 값을 정해 없을때 호출할 수 있음



# key 값을 순차적으로 추출하기
c = {'name':'smith', 'phone':'01012345678', 'birth': '1990'}
for k in c.keys():
    print(k) # name, phone, birth -> 키값을 한개씩 불러올 수 있음
    
# key값을 추출하여 리스트 만들기 : dictName.key()
list_c_keys = list(c.keys()) # 키값을 뽑은 후에 리스트로 감쌈 
print(list_c_keys) # ['name', 'phone', 'birth']


# value값을 추출하여 리스트 만들기 : dictName.values()
list_c_values = list(c.values())
print(list_c_values) 


# key, value 쌍으로 리스트에 넣기 : dictName.items()
list_c_items = list(c.items())
print(list_c_items) # [('name', 'smith'), ('phone', '01012345678'), ('birth', '1990')]

# key와 value값 모두 지우기 : dictName.clear()
d = {"name":"jaewon", "age":20, "location":"seoul", "lulu":[1,2,3,4,5]}
d.clear()
print(d) # {}


# 해당 key가 딕셔너리에 안에 있는지 확인하기(in) -> 있으면 True, 없으면 False 돌려줌
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print("name" in a) # True
print("birth" in a) # True
print("location" in a) # False