#def 함수이름(매개변수):
#   수행할_문장
#    return 반환값

#1
#a,b = map(int,input('두 수를 입력하세요:').split())
#print(add(a,b))     #이렇게 하면 add에 대해서 함수가 정의되지 않았기 때문에 오류가 남
def add(a, b):
    return a + b

x, y = map(int, input("두 수를 입력하세요: ").split())
print(add(x, y))

#2
def to_upper(s):
    return s.upper()

s = input()
print(to_upper(s))

#3
def list_len(lst):
    return len(lst)

lst = list(map(int, input().split()))
print(list_len(lst))

#4
def end(w):
    return w[0] == w[-1]

w = input()
print(end(w))

#5
def even(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x)
    return result

nums = list(map(int, input().split()))
print(even(nums))

#6
def f(s):
    return s.replace(" ", "").lower()

s = input()
print(f(s))

#7
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

x, y = map(int, input().split())
print(bigger(x, y))

#8
def most_common(lst):
    max_count = 0
    result = None
    for x in lst:
        if lst.count(x) > max_count:
            max_count = lst.count(x)
            result = x
    return result

nums = list(map(int, input().split()))
print(most_common(nums))

#9
def filter(words):
    result = []
    for w in words:
        if len(w) >= 3:
            result.append(w)
    return result

words = input().split()
print(filter(words))

#10
def max_of_three(a, b, c):
    three = [a, b, c]
    max_val = max(three)
    return max_val

a, b, c = map(int, input().split())
print(max_of_three(a, b, c))

#11
def clean_alpha(s):
    result = ''
    for ch in s:
        if ch.isalpha():
            result += ch.lower()
    return result

s = input()
print(clean_alpha(s))

#12
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input())
print(sum_to_n(n))

#13
def length_list(words):
    result = []
    for w in words:
        result.append(len(w))
    return result

words = input().split()
print(length_list(words))

#14
def count_even_odd(lst):
    even = 0
    odd = 0
    for x in lst:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

nums = list(map(int, input().split()))
print(count_even_odd(nums))

#15
def initials(s):
    words = s.split()
    result = ''
    for w in words:
        result += w[0].upper()
    return result

s = input()
print(initials(s))

#16
def who_is_pass(scores):
    for i in range(len(scores)):
        if scores[i] >= 60:
            print(i + 1, end=' ')

scores = list(map(int, input().split()))
who_is_pass(scores)

#17
def char_count(s):
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d

s = input()
print(char_count(s))

#18
def get_divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

n = int(input())
print(get_divisors(n))

#19
def longest_word(s):
    words = s.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

s = input()
print(longest_word(s))

#20
def find_char(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return i
    return '없음'

s = input()
ch = input()
print(find_char(s, ch))