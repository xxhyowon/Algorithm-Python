# 210226 https://programmers.co.kr/learn/courses/30/lessons/12904

def solution(s): # 효율성x
    temp = []
    for i in range(len(s)) :
        for j in range(1,len(s)+1) :
            if i<j and s[i:j] == (s[i:j])[::-1] :
                temp.append(j-i)
            if j<i and s[j:i] == (s[j:i])[::-1] :
                temp.append(j-i)
    return max(temp)


def palindrome(string):
    if len(string) <= 1:
        return True
    
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

def solution(s):
    for cut in range(len(s), 0, -1):
        for start in range(0, len(s)):
            cutStr = s[start:start+cut]
            if palindrome(cutStr) == True:
                return len(cutStr)
            
            if start+cut >= len(s):
                break

print(solution("abcdcba")) #7