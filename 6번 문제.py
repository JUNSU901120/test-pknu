class Car :
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car) :
    def method(self):
        print("서브 클래스")

myCar = Car()
mySedan = Sedan()  # 객체 이름을 mySedan으로 변경
myCar.method()
mySedan.method()
