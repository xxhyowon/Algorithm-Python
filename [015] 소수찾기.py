# 210108 소수찾기
# 1부터숫자 n 사이에 있는 소수의 개수를 반환

def solution(n): # 시간초과
    count = n-1
    for i in range(2,n+1) :
        for j in range(2,i) :
            if i % j == 0 :
                count -= 1
                break
    answer = count
    return answer