# 210120 위장

def solution(clothes):
    clothes_dic = {}
    answer = 1
    for clth in clothes:
        key = clth[1]
        value = clth[0]
        if key in clothes_dic:
            clothes_dic[key].append(value)
        else:
            clothes_dic[key] = [value]
    for key in clothes_dic.keys():
        answer = answer * (len(clothes_dic[key]) + 1)
    return answer - 1

#testcode
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) #5