# 정수 n개가 주어졌을 때 합을 구하는 함수 def solve(a: list) -> int

def solve(a):
    answer = 0
    for i in a:
        answer += i
    return answer
