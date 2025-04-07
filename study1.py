#1
print('Hello, Word!!')

#2
print('I love python!!')

#3 실수 하나를 입력받아 소수점 첫째 자리까지 출력하시오
num=float(input())
print("%.1f" %num)

#4 두 정수를 입력받아 두 수의 합을 출력하시오
a=int(input())
b=int(input())

print(a+b)

#5 두 정수를 입력받아 두 수의 사칙연산 결과를 출력하시오
a = int(input())
b = int(input())

print("%d+%d=%d" %(a, b, a+b))
print("%d-%d=%d" %(a,b,a-b))
print("%d*%d=%d" %(a,b, a*b) )
print("%d/%d=%d" %(a,b,a/b))

#6 (질문하기기)
print( 'I am a student' )

#7
name = (input("당신의 이름은?: "))
age = int(input("당신의 나이는?: "))
height = int(input("당신의 키는?: "))

print("이름은 %s, 나이는 %d살, 키는 %dcm입니다." % (name, age, height))

#8 (질문하기)
num=int(input())

print(num**0.5)
print(num**2)
print(num**3)

#9
a = 5
b = 2
c = a // b

print("c = %d" % c)
#(답: 2)

#10
x = "Python"
y = 3
z = x * y

print(z)
#답:1 (PythonPythonPython)

#11
x = "Hello"
y = 10
z = x + y

print(z)
#답: 에러발생 (문자랑 숫자를 더할 순 없음음)

#12
price = 1500

print(price, "원", sep='')
#답: 1500원 (sep의 의미= 구분자, 분리하여 출력한다)

#13
x = 7
y = 2
z = x / y

print("결과: %d" % z)
# 3.0 (정수 형식 지정자로 출력하면 소수점이 버려진다 ->d=정수, f=실수 )

#14
print(5 / 2)
print(5 // 2)
print(5 % 2)
#답:나누기-몫-나머지

#15
a = 10
b = 5
c = a // b

print("결과: %d" % c)
#답: 2

#16
num=int(input())

if num==0:
    print("0입니다")
elif num>0:
    print("양수입니다")
else :
    print("음수입니다")



#17
age = int(input("나이:"))

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")

#18

score = int(input("점수:"))
if score>= 90:
    print('A학점')
elif score >= 80:
    print('B학점')
elif score>=70:
    print('C학점')
elif score >= 60:
    print('D학점')
else:
    print('F학점')

#19
time = int(input( ))

if time <12:
    print("오전")
else:
    print("오후")

#20
num1=int(input())
num2=int(input())
num3=int(input())

if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>3:
    print(num2)
elif num3>num1 and num3>num2:
    print(num3)

#21
a=int(input())
b= int(input())
c=a+b

if c%2==0:
    print("짝수입니다")
elif c%2!=0:
    print("홀수입니다")

#22
num =int(input())

if num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    print(num)

#23
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")

#24
a= int(input("정수: "))
b=int(input("정수: "))

if abs(a-b)>10 :                    #abs는 절댓값을 의미한다
    print("타이가 10 이상입니다")
elif abs(a-b)<10:
    print("차이가 10 미만입니다")
else:
    print(" 두 수가 같습니다")

#25
a=int(input("정수: "))
b=int(input("정수: "))
c=int(input("정수: "))

if a%2==0 and b%2==0 and c%2==0:
    print("모두 짝수입니다")
elif a%2!=0 and b%2!=0 and c%2!=0:
    print("모두 홀수입니다")
elif a==0 or b==0 or c==0 :
    print("0은 포함될 수 없습니다")
else:
    print("홀수와 짝수가 섞여 있습니다")