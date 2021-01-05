# 200105 https://programmers.co.kr/learn/courses/30/lessons/12948
# 핸드폰 번호 마지막 네자리 제외하고 *로 바꾸기

def solution(phone_number):
    # numberLength = len(phone_number) #휴대폰 번호 전체 길이
    # lastFour = phone_number[-4:] #마지막 네자리 수
    # answer = '*'*(numberLength-4) + lastFour
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
    return answer

# testcode
print(solution("01033334444")) # *******4444
print(solution("027778888") # *****8888