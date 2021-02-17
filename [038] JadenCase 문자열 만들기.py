# 210217 https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    
    s += ' a' # 공백+문자
    j = 0
    answer = []
    
    for i in range(len(s)) : # 공백 뒷부분 부터 문자앞까지 나누어 담기
        if s[i] == ' ' and s[i+1] != ' ' :
            answer.append(s[j:i+1])
            j = i+1 
            
    answer = [w[0].upper()+w[1:].lower() for w in answer] # 첫 문자는 대문자, 그 외는 소문자
    answer = ''.join(answer)
    return answer[:-1] # 마지막 공백 제거

#testcode
print(solution("3people unFollowed me")) # "3people Unfollowed Me"
print(solution("jad en  case")) # "Jad En  Case"