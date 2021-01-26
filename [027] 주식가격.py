# 210126 주식가격 

def solution(prices):
    stack = [0]*len(prices)
    stackbox = []
    for i, price in enumerate(prices):
        while stackbox and price < prices[stackbox[-1]]:
            j = stackbox.pop()
            stack[j] = i - j
        stackbox.append(i)
    while stackbox:
        j = stackbox.pop()
        stack[j] = len(prices) - 1 - j
    return stack

# testcode
print(solution([1, 2, 3, 2, 3])) #[4, 3, 1, 1, 0]