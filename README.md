
##  함수에 사용된 global 변수를 class 에 적용한 예
``` python
result =0
def add(num):
    global result # result 를 global 로 선언해줘야 result에 값이 누적된다
    result += num
    return result

print(add(3))
print(add(7))

```

위의 내용 중 global result를 클래스에 적용하면
---


``` python
#렌트카 업체
class Car():
    def __init__(self):
        self.license=0  #운전자보험의 종합보험 이라고 가정하자

    def driving(self, driver):
        print("이 차의 운전자는 "+driver +" 씨는 운전가능," ,end="")
        self.license +=1
        print(" 라이센스가 {} 사용되었습니다 ".format(self.license))

kia = Car()
hyundae = Car()

kia.driving('Kim')
kia.driving('Hong')
hyundae.driving("Lee")
kia.driving('Park')
```

