itemlist = [] 
itemlist.append(64)

x = int(input())

while(sum(itemlist)>x):
    itemlist.sort()
    half = itemlist[0]/2
    if ((sum(itemlist)-half >= x)):
        itemlist[0] = half
    else:
        itemlist[0] = half
        itemlist.append(half)
print(len(itemlist))
