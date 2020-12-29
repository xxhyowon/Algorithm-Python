# 201229
# 직사각형 별 찍기 https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
#5 3
#2 2
for i in range(b) :
    print('*'*a)