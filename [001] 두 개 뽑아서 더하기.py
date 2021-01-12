# 201221 두 개 뽑아서 더하기
# 정수 배열 numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return

def solution(numbers):
    temp_list = []
    for i in range(len(numbers)):
        # for j in range(len(numbers)):
        #     if j > i : # j<i, j!=i 전부 가능
        for j in range(i+1, len(numbers)) : # j > i 일 때
            temp_list.append(numbers[i] + numbers[j]) # i번 인덱스와 j번 인덱스의 합을 빈 리스트에 추가
    answer = sorted(list(set(temp_list))) # 중복제거(set), 오름차순 정렬
    return answer

# testcode
print(solution([1, 2, 3, 4, 1])) # [2, 3, 4, 5, 6, 7]
print(solution([5, 0, 2, 7])) # [2, 5, 7, 9, 12]