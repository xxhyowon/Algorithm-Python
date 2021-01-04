# 210104
# 실패율

def solution(N, stages):
    result = {} 
    failureLate = 0
    answer = []
    for n in range(1,N+1) :
        challenger = 0 
        failer = 0

        # n 단계에서 challenger, failer 수 구하기
        for i in stages : # i == 도전하고 있는 단계
            if i > n : 
                challenger += 1
            elif i == n :
                challenger += 1
                failer += 1
            else : 
                pass

        # n단계 실패율 계산
        if challenger != 0 :
            failureLate = failer / challenger
        else :
            failureLate = 0 

        result[n] = fail # {n(단계) : n단계 실패율}

    sorted_result = sorted(result.items(), reverse = True, key = lambda item: item[1]) # value값(실패율값) 역순으로 정렬
    
    for key, value in sorted_result: # 단계값(key값) 담기
        answer.append(key)

    return answer

# testcode
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]