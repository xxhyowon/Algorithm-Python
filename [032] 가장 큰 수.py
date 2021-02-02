# 210202 가장 큰 수
# 0 또는 양의 정수가 담긴 배열이 주어졌을 때, 배열의 원소를 이어 붙여 만들 수 있는 가장 큰 수를 문자열로 return

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) # numbers의 원소는 0 이상 1,000 이하(3자리수까지 비교)
    answer = str(''.join(numbers))
    if answer == '0'*len(numbers) : # numbers가 0으로만 구성 된 경우
        return '0' # 만들 수 있는 가장 큰 수 는 0
    return answer

#testcode
print(solution([3, 30, 34, 5, 9])) #'9534330'
print(solution([0,0,0])) #'0'
