# 201221
# 두 개 뽑아서 더하기 https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    temp_list = []
    for i in range(len(numbers)):
        # j = 1
        # while j <= len(numbers)-1 :
        #     if j > i : 
        #         temp_list.append(numbers[i]+numbers[j]) 
        #         j += 1
        #     else :
        #         j += 1
        for j in range(len(numbers)):
            if i > j : #j가 i보다 큰 값일 때
                temp_list.append(numbers[i] + numbers[j]) #i번 인덱스와 j번 인덱스의 합을 빈 리스트에 추가
            else :
                pass
    answer = sorted(list(set(temp_list))) # 중복제거(set), 오름차순 정렬
    return answer


# testcode
print(solution([1, 2, 3, 4, 1]))
print(solution([5, 0, 2, 7]))