#1
name = input()
with open("name.txt", "a") as file:
    file.write(name)

#2
with open("hello.txt", "r") as file:
    line = file.readline()
print(line.strip())

#3
with open('data.txt','r') as file:
    text = file.read()
    words = text.split()
    print(len(words))


#4
with open('log.txt','r') as file:
    for line in file:
        if 'error' in line:
            print(line)

#5
with open('words.txt', 'r') as file:
    text = file.read()
    words = text.split()
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print(word_count)


#6
with open('num.txt', 'r') as file:
    nums = file.read()          
    num_list = nums.split()

with open('even.txt', 'w') as file:
    for n in num_list:
        if int(n) % 2 == 0:
            file.write(n + '\n')


#7
# student=[]
# with open ('student.txt','r') as file:
#     for line in file: