for letter  in ['a','b','c']:
    print(letter )
    
# 만약 인덱스번호를 얻고 싶다면
for letter  in enumerate(['a','b','c']):
    print(letter) 
    
#인덱스 번호가 보인다. 이제 내용과 인덱스번호를 따로 가져오고 싶다면
for  i, letter in enumerate(['a','b','c']):
    print('인덱스{}  내용 {}'.format(i , letter) )
    
for letter  in enumerate(['a','b','c'], start=1):
    print(letter) 
    
for letter  in enumerate(['a','b','c'], start=11):
    print(letter) 
# start=숫자 를 이용해 시작번호를 지정할 수도 있습니다
