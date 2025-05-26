def solution(string):
    answer = ''
    for i in string:
        if i not in answer:
            answer+=i
    return answer
input_string = str(input())
result = solution(input_string)
print(result)