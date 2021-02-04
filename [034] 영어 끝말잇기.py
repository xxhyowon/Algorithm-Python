#210204 영어 끝말잇기

def solution(n, words):
    words_list = []
    count = 0
    answer = [0, 0]
    for i, word in enumerate(words):
        count %= n
        if i >= 1: 
            if word in words_list or words_list[-1][-1] != word[0] : 
                answer = [count + 1, 1 + i//n]
                break
        count += 1
        words_list.append(word)
    return answer

#testcode
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"])) #[1,3]