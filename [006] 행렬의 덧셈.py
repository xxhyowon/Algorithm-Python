# 201228
# 행렬의 덧셈 https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    arr_sum = []
    for i in range(len(arr1)):
        a = [] # a를 초기화시켜줘서 행렬의 i번 인덱스와 i+1번 인덱스의 합을 구분
        for j in range(len(arr1[0])):
            a.append((arr1[i])[j]+(arr2[i])[j])
        arr_sum.append(a)
    return arr_sum

# testcode
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))