# 210205 점프와 순간 이동

def solution(n):
    answer = 1
    while n != 1 :
        if n % 2 != 0 :
            n -= 1
            answer += 1
        n = n//2
    return answer

#testcode
print(solution(5)) #2
print(solution(6)) #2