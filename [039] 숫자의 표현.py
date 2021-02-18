# 210218 https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(num):
    answer = 0
    
    for i in range(1, num//2+1):
        s = 0 # 연속된 자연수들의 합        
        while s < num: # 합이 num보다 작을 동안     
            s += i 
            i += 1 # 연속한 자연수(1이 증가한) 더하기
            
        if s == num: # 연속된 자연수들의 합으로 num을 표현 할 수 있으면
            answer += 1
            
    return answer + 1 # 15 = 15

#testcode
print(solution(15)) #4