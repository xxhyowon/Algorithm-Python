# 210111 최소공배수와 최대공약수
# 두 수의 최대공약수와 최소공배수를 반환

def solution(n, m):
    minNum = min(n,m)
    for i in range(minNum,0,-1):
        if n % i == 0 and m % i == 0 :
            break
    answer = [i, i*(n//i)*(m//i)]
    return answer

#testcode
print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]
print(solution(16, 12)) # [4, 48]