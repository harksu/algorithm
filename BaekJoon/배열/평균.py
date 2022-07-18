number = int(input())

list = list(map(int,input().split()))
max = max(list)

for i in range(number):
    list[i] = list[i]/max*100

average = sum(list)/number
print(average)

