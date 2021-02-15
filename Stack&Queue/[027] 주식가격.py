# 210126 주식가격 
# 주식가격이 초 단위로 기록된 배열 prices, 주식 가격이 떨어지지 않은 기간은 몇 초인지 return 

def solution(prices):

    times = []

    for i in range(len(prices)):
        s = 0 # 주식 가격이 떨어지지 않은 기간 초기화
        for j in range(i+1, len(prices)):
            s += 1
            if prices[i] > prices[j]: # 주식가격이 떨어졌으면
                break #break
        times.append(s)

    return times


# def solution(prices):
#     times = []
#     while prices :
#         price = prices.pop(0) # 시간초과
#         s = 0
#         for p in prices :
#             s += 1
#             if price > p :
#                 break
#         times.append(s)
#     return times

def solution(prices):
    times = []
    
    from collections import deque
    que_prices = deque(prices)
    
    while que_prices :
        price = que_prices.popleft()
        s = 0
        for n in que_prices :
            s += 1
            if price > n : # 주식가격이 떨어졌으면
                break
        times.append(s)

    return times

# testcode
print(solution([1, 2, 3, 2, 3])) #[4, 3, 1, 1, 0]