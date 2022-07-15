number = int(input())
count = 0
asnwer = number 
while (1):
    if(number<10):
        left = 0
    else:
        left = int(number/10)       
    right = number%10
    sum = (left+right)%10
    new_number = (right*10) + sum
    count += 1
    if(asnwer == new_number):
        print(count)
        break
    number = new_number
   
    

   