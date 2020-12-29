# 201225
# 내적 https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    innerProduct = 0
    for i in range(len(a)) :
        innerProduct += a[i]*b[i]
    answer = innerProduct
    return answer

# testcode
print(solution([1,2,3,4], [-3,-1,0,2]))
print(solution([-1,0,1], [1,0,-1]))