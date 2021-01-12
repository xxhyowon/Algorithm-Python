# 210112 다트 게임
# 점수|보너스|옵션으로 이루어진 문자열 3세트 합계 점수 return

def solution(dartResult):
    j = 0 # 숫자(점수) 인덱스 값 
    score = []
    bonus = {'S':1,'D':2,'T':3}

    for i in range(0,len(dartResult)) :

        # 점수,보너스 계산
        if dartResult[i] in bonus : # S, D, T 각 보너스마다 해당 세트 점수 1제곱, 2제곱, 3제곱
            score.append(int(dartResult[j:i])**bonus[dartResult[i]])
            j = i+1

        # 옵션 계산
        elif dartResult[i] == '#' : # 아차상(#) 해당 세트 점수 마이너스
            score[-1] = score[-1]*(-1)
            j = i+1
        elif dartResult[i] == '*' : # 스타상(*) 해당 세트 점수와 바로 전 세트 점수 각 2배
            if i > 2 :
                score[-1],score[-2] = score[-1]*2,score[-2]*2
            else : score[-1] = score[-1]*2 # 해당 세트 점수만 있을 때
            j = i+1
            
    answer = sum(score) # 총 합 == 각 세트 점수들의 합
    return answer

#testcode
print(solution('1S*2T*3S')) #23
print(solution('1D#2S*3S')) #5