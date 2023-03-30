n= int(input())
f=1
for i in range(2,n+1):
    f *= i 
    #팩토리얼 계산 
    while True:
        if str(f)[-1] == "0":
            f //= 10 
            #0이면 나눠서 없애주고
        else:
            break
    f%=100000000000000000
    #값이 너무 크니까, 그 다음 넘으면 사용안하게끔 조치
print((str(f)[-5:]))        


