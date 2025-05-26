#1
class Square:
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return self.length ** 2

s = Square(5)
print("넓이:", s.get_area())

#2
class Car :
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
    def show_info(self):
        print(f"자동차 색상: {self.color},속도 :{self.speed}")
c = Car("빨강", 100)
c.show_info()

#3
class Car:
    count = 0
    def __init__(self, color):
        self.color = color
        Car.count += 1

car1 = Car("빨강")
car2 = Car("파랑")

print("총 차량 수:", Car.count)

#4
class Car:
    def __init__(self):
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

class SportsCar(Car):
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 200:
            self.speed = 200

myCar = SportsCar()
myCar.upSpeed(250)
print("현재 속도(스포츠카):", myCar.speed)

#5

class Student:
    def __init__(self, name, age, mbti, mid, final):
        self.name = name
        self.age = age
        self.mbti = mbti
        self.mid = mid
        self.final = final

    def intro(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}입니다")
        print(f"{self.name}의 mbti는 {self.mbti}입니다")

    def __del__(self):
        print("이제 나 죽습니다")   #소멸자에서 끝나면 알아서 이제 나 죽습니다 결과값 나옴->일일이 프린트 이제 나 죽습니다 아님

genie = Student("genie", 20, "enfj", 95, 80)
alex = Student("alex", 23, "esfj", 60, 92)

genie.intro()
alex.intro()

print(f"\n현재 학생 수는? 2명 입니다\n")

if genie.mid > alex.mid:
    print(f"중간고사에서 더 높은 점수를 받은 사람은 {genie.name}이며, 점수는 {genie.mid}점입니다.")
else:
    print(f"중간고사에서 더 높은 점수를 받은 사람은 {alex.name}이며, 점수는 {alex.mid}점입니다.")

if genie.final > alex.final:
    print(f"기말고사에서 더 높은 점수를 받은 사람은 {genie.name}이며, 점수는 {genie.final}점입니다.")
else:
    print(f"기말고사에서 더 높은 점수를 받은 사람은 {alex.name}이며, 점수는 {alex.final}점입니다.")


#6
class Student:
    def __init__(self, name, mid, final):
        self.name = name
        self.mid = mid
        self.final = final

    def checkpass(self):
        total = self.mid + self.final
        if total >= 160:
            result = "합격"
        else: 
            result = "불합격"
        print(f"학생: {self.name}, 총점: {total}, 결과: {result}")

genie = Student("genie", 95, 75)
alex = Student("alex", 60, 90)

genie.checkpass()
alex.checkpass()

#7
class Student:
    def __init__(self,name,국어,수학,영어):
        self.name=name
        self.국어=국어
        self.수학=수학
        self.영어=영어

class HighSchoolStudent(Student):
    def get_grade(self):
        avg = (self.국어 + self.수학 + self.영어) / 3
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        else:
            grade = "F"
        print(f"학생: {self.name}, 평균: {avg:.2f}, 등급: {grade}")
genie = HighSchoolStudent("genie", 95, 88, 92)
alex = HighSchoolStudent("alex", 75, 80, 80)

genie.get_grade()
alex.get_grade()

#8
with open("student1.txt", "r") as f:
    lines = f.readlines()[1:]
    
    for line in lines:
        name, kor, math, eng = line.strip().split(',')
        student = HighSchoolStudent(name, int(kor), int(math), int(eng))
        student.get_grade()