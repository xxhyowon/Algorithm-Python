# 210122 https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book): 
    phone_book.sort(key = len) #길이 순으로 정렬
    for i,n in enumerate(phone_book) : # 길이 짧은 번호 n
        for num in phone_book[i+1:] : # n보다 길이 긴 번호 num
            if n == num[:len(n)] : # n이 num의 접두어이면
                return False # return False
    return True

#정렬 안하는 경우
def solution(phone_book):
    for i in range(len(phone_book)): 
        for j in range(i+1, len(phone_book)): 
            numLen = min(len(phone_book[i]), len(phone_book[j])) # 짧은 번호 길이구하기
            if phone_book[i][:numLen] == phone_book[j][:numLen]: 
                return False 
    return True

def solution(phone_book): #hash
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
    
#testcode
print(solution(["119", "97674223", "1195524421"])) #false
print(solution(["123","456","789"])) #true
print(solution(["12","123","1235","567","88"])) #false