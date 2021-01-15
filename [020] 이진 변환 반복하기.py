# 210115 이진 변환 반복하기
# 0과 1로 이루어진 문자열 s의 이진 변환 횟수와 변환 과정에서 제거된 모든 0의 개수를 배열에 담아 return

def solution(s):
    cnt_0 = 0 # 변환 과정에서 제거되는 0의 개수
    cnt_bin = 0 # 이진 변환의 횟수
    while s != '1' :
        cnt_0 += s.count('0') # 문자열s의 모든 0 제거
        s = bin(s.count('1'))[2:] # s = s에서 모든 0을 제거한 문자열의 길이
        cnt_bin += 1
    answer = [cnt_bin, cnt_0]
    return answer

# testcode
print(solution("110010101001")) #[3,8]
print(solution("01110")) #[3,3]
print(solution("1111111")) #[4,1]