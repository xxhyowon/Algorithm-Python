# 210104 실패율
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return, 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저

def solution(N, stages):
    result = {} 
    failureLate = 0 # 실패율
    answer = []
    for n in range(1,N+1) :
        challenger = 0 # 스테이지에 도달한 플레이어 수
        failer = 0 # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수

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
        else : # n단계에 도달한 유저가 없는 경우 해당 단계의 실패율은 0
            failureLate = 0 

        result[n] = failureLate # {n(단계) : n단계 실패율}

    sorted_result = sorted(result.items(), key = lambda item: (-item[1], item[0])) # 실패율값(value값==item[1]) 역순으로 정렬, 같은 값 있으면 key값(item[0]) 오름차순으로 정렬
    
    for key, value in sorted_result: # 단계값(key값) 담기
        answer.append(key)

    return answer

# testcode
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3,4,2,1,5]
print(solution(4, [4,4,4,4,4])) # [4,1,2,3]

# sorted_result = sorted(result.items(), key = lambda item: (-item[1], item[0]))

# {key : value}.items() > [(key, value)]

# lambda item : item[1]
# def sorted_failureLate(item) :
#   return item[1]
# for item in result.items() :
#   sorted_failureLate(item)