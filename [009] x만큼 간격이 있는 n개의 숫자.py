# 201231
# x만큼 간격이 있는 n개의 숫자 https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    temp_list = []
    for i in range(1, n+1):
        temp_list.append(x * i)
    answer = temp_list
    return answer

#testcode
print(solution(2, 5)) #[2,4,6,8,10]
print(solution(4, 3)) #[4,8,12]
print(solution(-4, 2)) #[-4,-8]