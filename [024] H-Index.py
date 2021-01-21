# 210121 H-Index

# def solution(citations):
#     citations.sort(reverse=True)
#     for i in range(len(citations)) :
#         if citations[i] <= (len(citations)-i) :
#             answer = citations[i]
#             break
#     return answer

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

#testcode
print(solution([3, 0, 6, 1, 5])) #3