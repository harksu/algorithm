number = int(input())
newlist = []
for i in range (number):
    lists = list(map(int,input().split()))
    count = lists[0]
    average = (sum(lists) - count)/(len(lists)-1)
    good = 0.00000000
    for i in lists:
        if i == count:
            continue
        if i > average :
            good += 1
    result = round(((good/count) * 100),3)
    newlist.append(result)
for i in newlist:
    print('%.3f'%i,end='')
    print('%')