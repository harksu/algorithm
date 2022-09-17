# 재배열을 할 때, a의 가장 작은 수를 b의 가장 큰 수와 맞도록 인덱스를 바꿔줘야 됨(b는 못바꾸니까 )

from audioop import minmax
from operator import index


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 가장 작은걸, b는 가장 큰 걸 곱해서 합에다가 더해 주고 연산에 들어간 원소들은 제거하면서 반복하면 되지 않을 까 ?
# 백준에서 조건으로 나오는 걸 굳이 과정까지 옮길 필요는 없는 것 같다, 그냥 결과랑 조건만 나오면 될 듯(이것도 굳이 a를 재배열 할 필요는 없는거니까)
result = 0
for i in range(n):
    min_value = min(a)
    max_value = max(b)
    result += (min_value * max_value)
    a.pop(a.index(min_value))
    b.pop(b.index(max_value))

print(result)
