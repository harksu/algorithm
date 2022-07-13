
T = int(input())
list = []
for i in range (1,T+1):
    num1,num2 = map(int,input().split())
    list.append(num1+num2)
for i in range (1,T+1):
    print('Case #{0}: {1}'.format(i,list[i-1]))
   
    