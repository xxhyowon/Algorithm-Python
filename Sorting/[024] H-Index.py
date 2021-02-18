# 210121 https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations = sorted(citations) # 오름차순 정렬
    n = len(citations) # 논문 개수 n
    for idx, c in enumerate(citations) :
        if c >= n-idx : # n-idx == 전체 논문 n개 중에서 c번이상 인용된 논문 개수
            return n-idx # 처음으로 c번이상 인용된 논문 개수(n-idx)가 c보다 같거나 작아질 때 n-idx값(c값아님) == H-Index
    return 0

def solution(citations):
    citations.sort(reverse=True) # 내림차순 정렬
    # print(list(enumerate(citations, start=1))) # [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 4), (7, 1)] : (i,c) == c번이상 인용된 논문이 i개
    # print(list(map(min,enumerate(citations, start=1)))) # [1, 2, 3, 4, 5, 4, 1] i(c번이상 인용된 논문 개수) >= c 이면 c값, i < c 이면 i값
    # 6번 이상 인용된 논문이 5개(5), 4번 이상 인용된 논문이 6개(4) > 5번 이상 인용된 논문이 5개
    answer = max(map(min, enumerate(citations, start=1))) # 최댓값 5 == H-Inex
    return answer

# #testcode
print(solution([1,4,6,6,6,6,6])) #5
print(solution([3, 0, 6, 1, 5])) #3