# 201223
# 하샤드 수 https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(arr):
    sum = 0
    for i in str(arr) : #arr 각 자릿수 차례로 순회
        sum += int(i) # 각 자릿수 합
    return arr % sum == 0 # arr을 각 자릿수의 합으로 나눴을 때 나머지가 0이면(하샤드 수이면) True

# testcode
print(solution(10))
print(solution(12))
print(solution(11))