n = int(input())
num1,num2,num3,num4,num5 = map(int,input().split())
list = []
list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
list.sort()
print('{0} {1}'.format(list[0],list[4]))

