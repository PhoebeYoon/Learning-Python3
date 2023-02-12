# 문자열 길이 구하기 : len()
mylength = 'Hello world'
print(len(mylength)) # 11

# 문자열 인덱싱
indexing = "Life is too short, You need Python"
print(indexing[3]) #  인덱스는 0번부터 시작하므로 3은 4번째 위치를 말한다 , 결과는 e
print(indexing[-1]) # 보통의 인덱싱은 양수이지만 마이너스일때는 뒤에서부터 시작한다는 의미로 -1은 뒤에서 부터 첫번째, 결과는 n

# 문자열 슬라이싱
slicing = "Life is too short, You need Python"
print(slicing[0:4]) # Life -> [x:y] x부터 y전까지 문자열을 뽑아옴(끝 번호 포함 안함)
print(slicing[:]) # Life is too short, You need Python
print(slicing[:4]) # Life
print(slicing[18:]) # You need Python
print(slicing[-1:7]) # Python

# 문자 갯수 세기(count)
count_str = "lalalalalballlballballballllblblblblaaaa"
print(count_str.count("l")) # 20 -> count_str 중 l의 갯수를 가져옴
# 위치 알려주기(find)
find_str = "python!"
print(find_str.find("!")) # 6 -> !표가 6번째 자리에 위치함
print(find_str.find("a")) # -1 -> a가 find_str안에 없음

# 문자열 삽입(join)
join_str = "python"
join_str = "python"
print(".".join(join_str)) # .으로 연결 / p.y.t.h.o.n 
print("-".join(join_str)) # - 으로 연결 /  p-y-t-h-o-n

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper()) # HI

# 대문자를 소문자로 바꾸기(lower) #python
a = "PYTHON"
print(a.lower())

# 공백지우기 
print('0123456789')
a = "     hi    "
print(a.strip()) # 결과는 hi, 양쪽 공백 지우기(strip) 
print(a.lstrip() +'-----') #왼쪽 공백 지우기(lstrip) /
print(a.rstrip()) #오른쪽 공백 지우기(rstrip)

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("short", "long")) # short를 long로 대치


# 문자열 나누기(split) : ()안에 있는 문자열을 기준으로해서 문자열을 나누고 결과값을 리스트 넣는다.
a = "Life is too short"
print(a.split()) # ['Life', 'is', 'too', 'short']

b = "a:b:c:d"
print(b.split(":")) # ['a', 'b', 'c', 'd']