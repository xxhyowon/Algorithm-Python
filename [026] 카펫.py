#210125 카펫

def solution(brown, red):
    for h in range(1, int(red**0.5)+1):
        if not red % h:
            w = red // h
        if 2*h + 2*w + 4 == brown:
            return [w+2, h+2]

#testcode
print(solution(24,24)) #[8, 6]