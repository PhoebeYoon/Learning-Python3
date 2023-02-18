## Python JSON
파이썬은 빌드인 패키지로 json를 갖고 있다. json 를 사용하려면 
```
import json
```
json는 자바스크립트의 표기법를 따른다 
json는 언뜻보기에 객체와 비슷해 보인다 

### Convert from JSON to Python
JSON를 Python으로 변환하려면 loads() 메소드가 필요하다   

``` python
import json

demo = '{"name":"Kim", "age":30, "city": "Seoul"}'. 
# 자세히보면 {} 가 ' ' 로 묶여져 있고 안에 있는 것들은 " "로 묶여있는 JSON string 이다
print(type(demo)) # <class 'str'> 이라고 나온다
print(demo["name"])  #딕셔너리가 아니므로 에러 발생

result = json.loads(demo)
print(result) #결과는 {'name': 'Kim', 'age': 30, 'city': 'Seoul'}
print(type(result)) # 결과는 <class 'dict'>
print(result['name']) #딕셔너리 이므로 이렇게해서 해당 값을 얻을 수 있다

```


### Convert from Python to JSON
python object를 JSON string으로 변환하기 위해서는 json.dumps() 메소드를 사용해야 한다
``` python
demo ={
    "name":"Kim", 
    "age":30, 
    "city": "Seoul"
}

# python의 딕셔너리 형태이다 정말 그런지 확인해 보자
print(demo['name']) # Kim 이라고 나온다
#이제 json 으로 변환해 보자
result =json.dumps(demo)
print(result) # 결과는 {"name": "Kim", "age": 30, "city": "Seoul"}
print(type(result)) # <class 'str'> 나온다

#print(result['name']) # 변환된 result 에서는 위와 같은 형태로는 값을 얻을 수 없다
print(result[:7])  # 결과는 {"name" 문자열이므로 문자열에 사용되는 기능을 사용할 수 있다

```
