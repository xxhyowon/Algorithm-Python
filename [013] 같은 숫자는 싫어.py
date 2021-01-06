# 210106 같은 숫자는 싫어
# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지 

def solution(arr) :
    answer = [arr[0]]
    for i in range(1, len(arr)) :
        if arr[i] == answer[-1] : 
            pass
        else :
            answer.append(arr[i])
    return answer

# testcode
print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) # [4,3]