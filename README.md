
### 주소록을 만들어보겠습니다.
##### 추가 설명을 넣었습니다.
##### 파일모드에 대한 설명은 아래쪽에 있습니다

``` python
import sys

class Person:

    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def info(self):
        print('{}, {}, {}'.format(self.name, self.phone, self.addr))
        
# 여기까지가 Person 클래스 끝

class AddressBook:
    def __init__(self):
        self.address_list = []
        self.file_reader()
        
    def file_reader(self):
        try:
            file = open('C:/python/1_final_pro/addressBook.csv', 'rt')  
            # 전체경로를 넣었습니다. csv 파일을 없어 저장내용을 확인합니다. 내용,내용 으로 되어 있는지요.
            # 콤마 사이에 있는 공백은 없애줍니다
        except:  # 예외 처리 (addressBook.csv 파일이 없을 때)
            print('addressBook.csv 파일이 없습니다.')
        else:  # 정상 처리 (addressBook.csv 파일이 있을 때)
            while True:
                buffer = file.readline()
                if not buffer:
                    break
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                addr = buffer.split(',')[2].rstrip('\n') #줄바꿈기호를 제거합니다
                self.address_list.append(Person(name, phone, addr))
            print('addressBook.csv 파일을 로드했습니다.')
            file.close()
            
            
    def file_generator(self):
        try:
            file = open('addressBook.csv', 'wt')  
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write('{},{},{}\n'.format(person.name, person.phone, person.addr))
            file.close()
    def menu():  # 실행하면 나오는 부분인데 아래 def에서 menu()를 부릅니다
        print('-' * 30)
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('프로그램 종료는 0번')
        print('-' * 30)
        choice = int(input('수행할 작업을 숫자로 입력하세요 >>> '))
        return choice

    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()

    def run(self):
        while True:
            choice = AddressBook.menu() # 위에 있는 menu()를 보세요
            if choice == 0: self.exit()
            elif choice == 1: self.insert()
            elif choice == 2: self.delete()
            elif choice == 3: self.update()
            elif choice == 4: self.search()
            elif choice == 5: self.printAll()
            else: print('없는 명령입니다. 확인 후 다시 입력하세요.')
    
    def insert(self):
        print('=== 신규 주소록 생성 ===')
        name = input('새 이름 입력 >>> ')
        phone = input('새 전화번호 입력 >>> ')
        addr = input('새 주소 입력 >>> ')
        if name and phone and addr:  # and으로 연결하여 3개의 값이 모두 입력되면

            self.address_list.append(Person(name, phone, addr))  # 삽입
            self.file_generator() #새로운 내용을 파일로 저장하는 처리를 합니다
            print('새 주소가 정상적으로 등록되었습니다.')
        else:  # 내용이 누락되면 저장되지 않도록 합니다
            print('입력값이 부족하여 주소록이 생성되지 않았습니다.')

    def delete(self):
        print('=== 기존 주소록 삭제 ===')
        name = input('삭제할 이름 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 삭제를 취소합니다.')
            return
        deleted = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다.'.format(self.address_list[i].phone))
                if input('정말로 삭제하시겠습니까 ?(y/n) >>> ').upper() != 'Y':  # 대소문자를 통일하기 위해 upper() 사용
                    continue  # 'Y'와 같지않으면 '참'이 되는 구조로 'N'가 입력되면 for문으로 되돌아가서 다음 사람을 검색
                self.address_list.pop(i)  # 삭제
                deleted = True
                print('{}의 정보를 삭제했습니다.'.format(name))
                self.file_generator()
                break
        if not deleted:
            print('{}의 정보가 삭제되지 않았습니다.'.format(name))

    def update(self):
        print('=== 기존 주소록 수정 ===')
        name = input('수정할 이름 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 수정을 취소합니다.')
            return
        updated = False
        for i, person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다.'.format(self.address_list[i].phone))
                if input('수정할까요?(y/n) >>> ').upper() != 'Y':
                    continue  # for문으로 되돌아가서 다음 사람을 검색
                new_phone = input('변경할 전화번호 입력 >>> ')
                if new_phone:  # 입력이 있으면
                     self.address_list[i].phone = new_phone  # 입력된 내용으로 변경
                new_addr = input('변경할 주소 입력 >>> ')
                if new_addr:
                    self.address_list[i].addr = new_addr
                updated = True
                print('주소록이 수정되었습니다. 수정된 주소록의 내용을 확인하세요.')
                self.address_list[i].info()
                self.file_generator()
                break
        if not updated:
            print('{}의 정보가 수정되지 않았습니다.'.format(name))

    def printAll(self):
        print('=== 전체 연락처 출력 ===')
        for person in self.address_list:
            person.info()
        print('총 {}개의 주소록이 있습니다.'.format(len(self.address_list)))

    def search(self):
        print('=== 주소록 검색 ===')
        name = input('찾을 이름을 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 검색을 취소합니다.')
            return
        exist = False
        for person in self.address_list:
            if name == person.name:
                person.info()
                exist = True
        if not exist:
            print('{}의 정보가 없습니다.'.format(name))


    def search(self):
        print('=== 주소록 검색 ===')
        name = input('찾을 이름을 입력 >>> ')
        if not name:
            print('입력된 이름이 없어 검색을 취소합니다.')
            return
        exist = False
        for person in self.address_list:
            if name == person.name:
                person.info()
                exist = True
        if not exist:
            print('{}의 정보가 없습니다.'.format(name))

#여기까지가 class AddressBook 종료 


myapp = AddressBook() 
myapp.run() 

```

> 만약 파일읽기에서 _UnicodeDecode\Error 'utf-8' codec can't decode byte 0xb9 in position 0_ 발생하면   
> file = open('/경로/addressBook.csv', 'r',<b>encoding='cp949'</b>) 로 넣어준다 encoding 에러이다

#### Character   Meaning
```
'r'     open for reading (default)
'w'     open for writing, truncating the file first
'x'     open for exclusive creation, failing if the file already exists
'a'     open for writing, appending to the end of the file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)
'U'     universal newlines mode (deprecated)

기본 읽기모드는 'r' 인데, 위에서 사용된 'rt'와 동일합니다
```


