# 201230
# 제일 작은 수 제거하기 https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    if arr == [] :
        arr.append(-1)
    answer = arr
    return answer

def solution(arr): # 최솟값이2개이상
    minimum = min(arr)
    while minimum in arr:
        arr.remove(minimum)
    if arr == [] :
        arr.append(-1)
    answer = arr
    return answer

# testcode
print(solution([4,3,2,1])) #[4,3,2]
print(solution([10])) #[-1]
print(solution([-5,-5,-5,3])) #[3]