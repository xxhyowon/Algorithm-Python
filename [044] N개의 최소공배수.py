# 210225

def solution(arr):
    s = arr[0]
    for i in range(1,len(arr)) :
        minN = min(s,arr[i])
        for j in range(minN,0,-1) :
            if s % j == 0 and arr[i] % j == 0 :
                break
        s = j*(s//j)*(arr[i]//j)
    return s

#testcode
print(solution([2,6,8,14])) #168