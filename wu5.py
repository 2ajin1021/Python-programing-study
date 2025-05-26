#원섭, 세희, 상근, 숭이, 강수 점수가 순서대로 주어진다
#40점 이상이면 그대로 자기 점수 40점 아래면 보충수업 받는다는 조건하에 항상 40점

score = 0
for i in range(5):
    testscore = int(input())
    if testscore >= 40:
        score += testscore
    elif testscore <40:
        score += 40
print(score//5)