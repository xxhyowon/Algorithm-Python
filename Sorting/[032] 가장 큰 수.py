# 210202 https://programmers.co.kr/learn/courses/30/lessons/42746
# 0 또는 양의 정수가 담긴 배열이 주어졌을 때, 배열의 원소를 이어 붙여 만들 수 있는 가장 큰 수를 문자열로 return

def solution(numbers):

    numbers = [str(n) for n in numbers] # 문자열로 변환
    numbers = [n*3 for n in numbers] # numbers의 원소는 0 이상 1,000 이하, 최소 세자리이상 비교할 수 있도록 문자열 세 번 반복
    numbers.sort(reverse=True) # 세 번 반복한 문자열로 내림차순 정렬
    numbers = [n[:len(n)//3] for n in numbers] # 세 번 반복한거 원래길이로 만들어서
    answer = ''.join(numbers) # 이어 붙이기

    if answer == '0'*len(numbers) : # numbers가 0으로만 구성 된 경우
        return '0' # 만들 수 있는 가장 큰 수 는 0
    return answer

def solution(numbers):
    numbers = list(map(str, numbers)) # 문자열로 변환
    numbers.sort(key=lambda x:x*3, reverse=True) # 문자열 세 번 반복한 값 기준으로 내림차순 정렬
    answer = str(''.join(numbers))

    if answer == '0'*len(numbers) :
        return '0'
    return answer

#testcode
print(solution([3, 30, 34, 5, 9])) #'9534330'
print(solution([0,0,0])) #'0'