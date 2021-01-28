# 210128 124나라의 숫자

def solution(n):
    answer = ''
    while n > 0 :
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer

#testcode
print(solution(3)) #4
print(solution(30)) #244
print(solution(64)) #1441
