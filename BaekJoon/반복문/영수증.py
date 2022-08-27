
total = int(input())
count = int(input())
answer = 0
for i in range(count):
    a,b=map(int,input().split())
    answer += (a*b)
if(answer == total):
    print('Yes')
else:
    print('No')
