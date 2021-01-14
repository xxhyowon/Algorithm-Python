# 210114 비밀지도

def solution(n, arr1, arr2):
    base2_arr1 = []
    base2_arr2 = []
    answer = []
    for i in range(n) :
        arr1_s = ''
        arr2_s = ''
        while len(arr1_s) != n or len(arr2_s) != n:
            arr1_s += str(arr1[i] % 2)
            arr2_s += str(arr2[i] % 2)
            arr1[i] //= 2
            arr2[i] //= 2
        
        base2_arr1.append(arr1_s)
        base2_arr2.append(arr2_s)
    
    for i in range(n) :
        s = ''
        for j in range(n) :
            if base2_arr1[i][j] == '1' or base2_arr2[i][j] == '1' : 
                s += '#'
            else : s += ' '
        answer.append(s[::-1])
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2): # arr1, arr2 zip()으로 묶어주기
        a12 = str(bin(i|j)[2:]) # i or j 이진수 문자열(binary) 변환, 필요없는 부분(b0) slicing
        a12=a12.rjust(n,'0') # a12 오른쪽 정렬, n보다 길이가 작으면 앞에 '0' 추가(전체길이가 n이 되도록)
        a12=a12.replace('1','#') # 1이면 #,
        a12=a12.replace('0',' ') # 0이면 공백으로 변환 후
        answer.append(a12) # answer에 추가
    return answer

# testcode
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2)) # ["#####","# # #", "### #", "# ##", "#####"]

# zip()
# number = [1,2,3,4]
# name = ['a','b','c','d']
# for number, name in zip(number, name) :
#     print(number,':',name)