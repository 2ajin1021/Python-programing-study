#1
score = int(input())
if score%2==0:
    scoreresult='짝수이고'
elif score%2!=0 and score!=0:
    scoreresult='홀수이고'
elif score==0:
    scorereult='zero이고'
    primer=False

primer=True
if score<2:
    primer=False
else:
    for i in range(2,score):
        if score %i==0:
            primer=False
        break
if primer==True:
    primeresult='prime입니다'
else:
    primeresult='prime이 아닙니다'
print('%d은 %s %s'%(score,scoreresult,primeresult))

#2
add=0
for i in range(1,101):
    if i%2==0:
        add+=i
print('1부터 100까지의 짝수 합은 %d'%add)

#3
score=int(input('몇 명에 대한 입력을 받겠습니까?:'))

#4
string=input()
count=0
for word in string:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

max_word = max(count, key=count.get)
max_count = count[max_word]

print("가장 많은 철자는 ", max_word, "이고, ", max_count, "번 나왔어요.", sep='')

#5
subject=input()


#6
nums=int(input())