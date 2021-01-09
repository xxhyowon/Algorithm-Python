# 210107 키패드 누르기
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 연속된 문자열 형태로 return

def solution(numbers, hand):    
    lastL = 10  # 마지막 왼손가락 위치
    lastR = 11 # 마지막 오른손가락 위치
    a = {1:(0,3), 2:(1,3), 3:(2,3), 4:(0,2), 5:(1,2), 6:(2,2), # {손가락 위치 번호 : (x,y)}
         7:(0,1), 8:(1,1), 9:(2,1), 0:(1,0), 10:(0,0), 11:(2,0)}
    answer = ''
    for i in numbers :
        distanceL = 0  # 왼손과의 거리 **for문 안에서 초기화 해주기
        distanceR = 0 # 오른손과의 거리 
        if i in [1,4,7] : # 1,4,7은 왼손
            lastL = i
            answer += 'L'
        elif i in [3,6,9] : # 3,6,9는 오른손
            lastR = i
            answer += 'R'
        else :
            for j in range(2): # 2,5,8,0은 가까운 손
                distanceL += abs(a[i][j]-a[lastL][j]) # 거리 = x값 차이 + y값 차이(가로 거리 차이 + 세로 거리 차이)
                distanceR += abs(a[i][j]-a[lastR][j])
            if distanceL < distanceR :
                lastL = i
                answer += 'L'
            elif distanceL > distanceR :
                lastR = i
                answer += 'R'
            else : # 거리가 같으면 오른손잡이는 오른손, 왼손잡이는 왼손 엄지손가락 사용
                if hand == "right" :
                    lastR = i
                    answer += 'R'
                else :
                    lastL = i
                    answer += 'L'
    return answer

# testcode
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")) # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left")) # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")) # "LLRLLRLLRL"