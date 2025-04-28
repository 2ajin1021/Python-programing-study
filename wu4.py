num = input().split()
A = int(num[0])
B = int(num[1])
C = int(num[2])

if A < B :
    if B<C :
        print(B)
    elif C<A:
        print(A)
elif B <A :
    if A<C:
        print(A)
    elif C<B:
        print(B)
else : print(C)


#오름차순을 사용해서 코드 짜보기
num = list(map(int, input().split()))
num.sort()
print(num[1])
#if문으로 풀기
num = list(map(int, input().split()))
A = num[0]
B = num[1]
C = num[2]

if (A >= B and A <= C) or (A >= C and A <= B):
    print(A)
elif (B >= A and B <= C) or (B >= C and B <= A):
    print(B)
else:
    print(C)
