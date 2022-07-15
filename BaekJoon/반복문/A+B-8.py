
T = int(input())
list= []
num1s=[]
num2s=[]
for i in range (1,T+1):
    num1,num2 = map(int,input().split())
    num1s.append(num1)
    num2s.append(num2)
    list.append(num1+num2)
for i in range (1,T+1):
    print('Case #{0}: {1} + {2} = {3}'.format(i,num1s[i-1],num2s[i-1],list[i-1]))
   
    