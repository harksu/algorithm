
num1,num2,num3 = map(int,input().split())
price = 0
bigNumber = 0
if (num1 == num2 == num3):
    price = 10000+ num1 * 1000
elif (num1 == num2 or num1 == num3):
    price = 1000+ num1 * 100
elif (num2 == num3):
    price = 1000+ num2 * 100
else:
    if(num1 >= num2 and num1 >= num3):
        bigNumber = num1
    elif(num2 >= num1 and num2 >= num3):
        bigNumber = num2
    else:
        bigNumber = num3
    price = bigNumber * 100

print(price) 

#이거 근데 클린코드 있을 것 같은데 
