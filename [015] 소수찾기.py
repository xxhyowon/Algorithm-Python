# 210108 소수찾기
# 1부터숫자 n 사이에 있는 소수의 개수를 반환

def solutionfail(n): # 시간초과
    count = n-1
    for i in range(2,n+1) :
        for j in range(2,i) :
            if i % j == 0 :
                count -= 1
                break
    answer = count
    return answer

import math

def solution(n): # 에라토스테네스의 체(sqrt(n) 이하의 수만 확인)
    num = set(range(2,n+1)) # 2부터 n+1까지 모든 수들의 집합
    for i in range(2, int(math.sqrt(n))+1): # 2부터 n제곱근까지 순회하면서
        num -= set(range(i*2, n+1, i)) # 집합num에서 i 배수 제거
    answer = len(num) # 집합num에 남아있는 수 == 소수
    return answer

#testcode
print(solution(10)) #4
print(solution(5)) #3
print(solution(10000)) #1229