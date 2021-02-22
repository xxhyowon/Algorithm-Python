# 210120 https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clothes_dict = {}

    for c in clothes:
        if c[1] not in clothes_dict : # 새로운 의상 종류라면
            clothes_dict[c[1]] = 2 # 의상 +1, 안입는 경우 +1
        else:
            clothes_dict[c[1]] += 1 # 의상 +1
            
    cnt = 1
    for num in clothes_dict.values():
        cnt *= num

    return cnt - 1 # 전부 안 입는 경우 -1

#testcode
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) #5