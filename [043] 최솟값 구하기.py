# 210224

def solution(A, B): 
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])

#testcode
print(solution([1,4,2],[5,4,4])) #29