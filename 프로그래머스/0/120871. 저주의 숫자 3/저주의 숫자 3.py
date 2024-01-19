def solution(num):
    return list(filter(lambda x: (x % 3 != 0) and ('3' not in str(x)), range(1000)))[num-1]

solution(15)

