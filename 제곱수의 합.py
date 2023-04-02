n = int(input())

#처음 수에서 제곱근을 구하고, 카운트 + 1
#그 제곱근에서 -1을 빼서 제곱하고 원래수에서 빼서 0보다 크면 카운트 +1,뺀값을 원래값으로 갱신하고
# 0 이하가 될 대 까지 계속반복
value = int(n**(1/2))
count = 0
while (1):
    print(n,value,count)
    n -= (value * value) #제곱근 빼고 남은 값으로
    if(n<=0):
        if(n==0):
            count +=1
            break
        elif(value==1):
            break
        else:
            n += (value * value)#다시 돌려놓고
            value -=1
            continue
    count +=1
print(count)
   
  
    
#11같이 제곱근이 1이 아닌 경우는 1로 계속 뺄 수 있다.
#만약 뺐는데 0보다 작다면 근데 value는 1보다 크다면 1빼고 다시 해보면 되는건데129

##무조건 제곱근으로 빼는게 최소일 보장없음 ex> 32

#이 문제 틀림 dp를 공부해보자..^^ 
n = int(input())
dp = [0 for i in range(n + 1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
    s = []
    for j in square:
        if j > i:
            break
        s.append(dp[i - j])
    dp[i] = min(s) + 1
print(dp[n])