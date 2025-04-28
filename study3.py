# num = input().split()
# A=int(num[0])
# B=int(num[1])
# C=int(num[2])
num = input().split()
A = int(num[0])
B = int(num[1])
C = int(num[2])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


##리스트

#1
num = [1,2,3,4,5]
print([-1])

#2
num = [3,6,9]
num.append(12)
print(num)

#3
num = int(input("몇번 입력받을래?:"))
list=[1,2,4,5]
list.append(num)



#4
num = [1,2,3,4,5]
if n in num:
    if n%2==0:
        print(i)

#5
num=[10,2,5,8]

#6
nums=list(map(int,input("정수를 입력하세요:").split()))
even=[]
odd=[]
if i in nums:
    if i%2==0:
        

#7
words = input().split()
lengths = []
for word in words:
    if (word == words[-1]):
        print(len(word), end='')
        break
    print(len(word), end=', ')

#8
list=[0,1,0,2,3,0]
print(list.count(0))

#9
num = int(input("정수를 입력하세요:"))

#10
lst = [1, 2, 3, 4, 5]
print(lst[::-1])

##튜플

#1
tpl=[10,20,30]
print([1])

#2
tup1=[1,2]
tup2=[3,4]
print(tup1+tup2)

#3
tpl=tup(map(int.input().split()))
print(tpl.max())
print(tpl.min())

#4
tpl=tup(map(int.input().split()))


#5
