# warm up 백준10869번

# a = int(input( "숫자를 입력하세요:"))
# b = int(input( "숫자를 입력하세요:"))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# a = int(input("1<=a<=100000인 자연수:"))
# b = int(input("1<=a<=100000인 자연수:"))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)


# A, B = input().split()
# A = int([0])
# B = int([1])

# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)


## 스터디 2주차 문제

#1
for i in range (1,11):
    print("%d"%i, end='')

#2
a = int(input("정수를 입력하세요:"))
for i in range(1, a+1):
    print(i)

#3
a=int(input("정수를 입력하세요:"))
for i in range (1,a+1):
    if i%2==0:
        print(i)

#4
i =0
dan =0
dan = int(input('구구단 몇 단을 계산할까요?:'))

for i in (1,10):
    print('%d x %d = %d' %(dan,i,dan*i))

#5
a=int(input("정수를 입력하세요:"))
for i in range(1,a+1):
    print(a=a+i)

#6

for i in range(1,10):
    print('%d x %d = %d' %(2, i, 2*i))

#7
num=int(input("정수를 입력하세요:"))
for i in range(1, num+1):
    if num%i==0:
        print(i)

#8
a=int(input("정수를 입력하세요:"))
b=int(input("정수를 입력하세요:"))
for i in range(a, b+1):
    print(i)

#9
for i in range(1,101):
    if i%3==0:
        print(i)

#10
a= int(input("정수를 입력하세요:"))
for i in range(1,a+1):
    print(a=a*i)


#11
a=int(input("높이를 입력하세요:"))
for i in range(1,a+1):
    print('*'*i)

#12
for i in range(1, 6):
    print("2 * %d = %d" % (i, 2 * i), end=' ')
    if i + 5 != 10:
        print("2 * %d = %d" % (i + 5, 2 * (i + 5)))
    else:
        print()

#13
s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")

#2번째 풀이 방법
s = input("")
length = len(s)
flag = False
for i in range(length // 2):
    if s[i] != s[length - i - 1]:
        break
else:
    flag = True

if flag:
    print("YES")
else:
    print("NO")

#14
n = int(input())
for i in range(n):
    print("%s%s" % (' ' * (n - i - 1), '*' * (2 * i + 1)))

#15
a = int(input("정수를 입력하세요:"))
for i in range(a):
    print(" " * i + "*" * (2 * (n - i) - 1))

for i in range(1, n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))