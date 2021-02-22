# 210222 https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    num = [int(a) for a in s.split(' ')]
    return str(min(num))+' '+str(max(num))

#testcode
print(solution("-1 -2 -3 -4")) #"-4 -1"