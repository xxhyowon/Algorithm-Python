# 210122 전화번호 목록

def solution(phone_book):
    phone_book.sort(key = len)
    for i in range(len(phone_book)) :
        a = len(phone_book[i])
        for b in phone_book[i+1:] :
            if phone_book[i] == b[:a] :
                answer = False
                break
            else : 
                answer = True
        if answer == False : 
            return False
            break
    return answer

#testcode
print(solution(["119", "97674223", "1195524421"])) #false
print(solution(["123","456","789"])) #true
print(solution(["12","123","1235","567","88"])) #false