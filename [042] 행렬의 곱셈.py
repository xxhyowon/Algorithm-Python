# 210223 https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    
    import numpy as np
    arr2 = np.swapaxes(arr2,0,1) # 전치행렬 만들기
    answer = []
    for i in range(len(arr1)) :
        temp_list = [] 
        for j in range(len(arr2)) :
            s = 0
            for a,b in zip(arr1[i],arr2[j]) :
                s += a*b
            temp_list.append(int(s))
        answer.append(temp_list)
    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])) #[[22, 22, 11], [36, 28, 18], [29, 20, 14]]