# #1 
# a = "hello"
# b = ['h', 'e', 'l','l','o']
# if a == b :
#     print(True)
# else: print(False)

# #2
# print("abc"+"123")

# #3
# print("ha"*3)

# #4
# word= "Python"
# print(len(word))

# #5
# word="hello"
# print(word.upper())

# #6
# word ="Python Is Fun"
# print(word.swapcase())

# #7
# word = "welcome to my place"
# print(word.title())

# #8
# word = input("문자를 입력하시오:")
# if word.islower():
#     print("소문자입니다")
# elif word.isupper():
#     print("대문자입니다")
# elif word.isdigit():
#     print("숫자입니다")

# #9
# word = 'banana'
# print(word.count('a'))

# #10
# # word = "hello world"
# # a = print(word.find('0'))
# # print("'0'의 첫 번째 인덱스는 %d이고, 마지막 인덱스는 %d입니다." %())

# #11
# print("a,b,c".split(','))

# #12
# print(" ".join(['hi', 'i\'m', 'genie']))

# #13
# word = " hello world"
# print(word.strip())

# #14
s = input()

first = s.find("@")
second = s.find("@", first + 1)
if second == -1:
    print("없음")
else: print(second)

# #15
# print("###data#science###".strip('#'))
print("###data#science###".replace("#","")) #이러면 가운데에 있는 #도 다 사려져서 조건에 부합하지 않음


# #16
# word = input().strip()
# print(word.find('a'))

# #17
# word = input().strip()
# word().split('')
# print(len(word[0]), len(word[1]))

# #19
# s = input().strip()
# print(s[0] == s[-1])

#20
s = input().replace(" ", "")
index = s.find('a')

while index != -1:
    print(index, end=' ')
    index = s.find('a', index + 1)

#split은 문자열을 리스트로 join은 리스트를 문자열로 바꾸는건가 둘이 아예 상성이 반대되는 것
