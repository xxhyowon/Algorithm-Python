# 210113 3진법 뒤집기

def solution(n):
    reverse_base3 = []
    base10 = []
    
    while n != 0 :
        reverse_base3.append(n % 3)
        n = n//3
        
    for i in range(1, len(reverse_base3)+1) :
        base10.append(reverse_base3[-i] * 3**(i-1))
    answer = sum(base10)
    return answer

#testcode
print(solution(45)) #7
print(solution(125)) #229