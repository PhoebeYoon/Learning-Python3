## 패키지( Packages )
1. 패키지란 특정한 과제(task)을 수행하기 위한 다양한 기능을 포함하는 컨테이너이다 
2. 많은 양의 코드를 하나의 파일에 담는다면 코드는 look messy! ( 엉망으로 보일 수 있고 관리도 어렵다)
3. 대신 관련코드를 패키지에 함께 보관하되 코드을 여러 파일로 분리한다. 이렇게 해서 코드를 재사용할 수도 있다
4. 파이썬에서는 (.) 도트연산자를 사용하여 패키지에서 모듈을 가져올 수 있다
5. 패키지를 보면 마치 계층구조로 만들어진것 같고 확장자가 .py 인 파일은 모듈로 불러온다


### 패키지에서 모듈 불러오기 (Importing module from a package)

   <img width="481" alt="스크린샷 2023-02-18 오후 4 19 07" src="https://user-images.githubusercontent.com/48478079/219850054-33783a32-262f-4e6b-a3c2-f915d48cb64a.png">


###### (사진출처 : https://www.programiz.com/python-programming/package)

위 이미지를 예시로 보면, 
``` python
import Game.Level.start
```
이렇게 기술해서 start 모듈을 가져오면 된다

### 패키지를 불러오기 않고 모듈 불러오기

``` python
from Game.Level import start
```

### ```  __init__.py  ```를 사용하는 이유
디렉토리를 만들고 폴더안에 .py 를 넣었다고 해서 이것이 패키지로 간주되어는 것은 아니다. 파이썬이 패키지로 간주하려면 디렉토리안에 __init__.py 라는 이름의 파일이 있어야 한다. 이 파일은 빈 파일일 수 있지만 일반적으로 해당 패키지의 초기화코를 넣는다
> 파이썬 3.3 버전부터는 ㅡㅡinitㅡㅡ 파일이 없어도 패키지로 인식하지만 하위버전과의 호환을 위해서 넣어주는 것이 좋다고 생각한다

### 이제 패키지를 만들어보자
game 이라는 이름의 패키지를 만들자 ( 다른 분들이 game 이라는 이름을 좋아하시는 듯해서 그냥 game으로 하자 )
<img width="158" alt="스크린샷 2023-02-18 오후 6 22 36" src="https://user-images.githubusercontent.com/48478079/219852867-102e3080-5442-49f6-a97d-3b921b5a920b.png">
여기서 빨간색 테두리는 직접만들어야 하는 것들이다.
1) package 폴더생성
2) cd package 이동해서 game폴더, main.py 생성
3) cd game 이동해서 characters폴더, ㅡㅡinitㅡㅡ.py 생성
4) cd character 이동해서 enemy.py, player.py, ㅡㅡinitㅡㅡ.py 생성, 일단 모든 파일은 빈파일로 하고 나중에 내용을 삽입할 것이다
그래서, package > game > characters 
###### \package폴더 안에   
<img width="120" alt="스크린샷 2023-02-18 오후 6 33 12" src="https://user-images.githubusercontent.com/48478079/219853099-dbf7411a-7b4c-4f89-8b23-5b232717511e.png">   

###### \game폴더 안에  
<img width="120" alt="스크린샷 2023-02-18 오후 6 33 59" src="https://user-images.githubusercontent.com/48478079/219853113-610bc9f7-52f2-4b89-9482-b088e69d4290.png">   

###### \characters폴더 안에  
<img width="120" alt="스크린샷 2023-02-18 오후 6 34 23" src="https://user-images.githubusercontent.com/48478079/219853183-45eee245-e8f7-4411-896b-ce9823a8b451.png">

나머지 파일들은 나중에 자동으로 생성된다 


``` python
# enemy.py 
def get_enemy_info():
    print("나는 적군이다")
```

``` python
# player.py
def player_info():
    print("나는 아군이다"
```

ㅡㅡinitㅡㅡ.py 는 내용을 삽입하지 않고 파일만 만든다


``` python

```

``` python

```
