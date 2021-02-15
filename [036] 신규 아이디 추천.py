# 210215 https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    new_id = new_id.lower() # 소문자로 치환
    
    new_id = ''.join(re.findall('[a-z0-9-_.]+', new_id)) # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 제외 모든 문자 제거

    while '..' in new_id : #  마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
         new_id = new_id.replace('..','.')
            
    if new_id[0] == '.' and len(new_id) > 1 : #마침표(.)가 처음이나 끝에 위치한다면 제거
         new_id = new_id[1:]
    if new_id[-1] == '.' :
        new_id = new_id[:-1]
    
    if new_id == '' : new_id = 'a' # 빈 문자열이라면 "a"를 대입
        
    if len(new_id) >= 16 : # 길이가 16자 이상이면 첫 15개의 문자 제외 나머지 문자들 모두 제거
        new_id = new_id[:15]
    if new_id[-1] == '.' : # 제거 후 마침표(.)가 new_id의 끝에 위치한다면 제거
        new_id = new_id[:-1]
    
    if len(new_id) <= 2 : # 길이가 2자 이하라면, new_id의 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
        new_id += new_id[-1]*(3-len(new_id))
    
    return new_id

#testcode
print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"