t = int(input())
state = 3  # 인덱스로 접근하는게 더 쉬울 것 같음
gostate = list(str(input()))  # 입력 양식 다르다고 틀리는거 억깐데
x = 0
y = 0
xlist = []
ylist = []
postionlist = [{'x': 0, 'y': 0}]

for i in gostate:
    if i == 'L':
        state = ((state - 1) % 4)
    elif i == 'R':
        state = ((state + 1) % 4)
    elif i == 'F':
        if (state == 0):
            x -= 1
            postionlist.append({'x': x, 'y': y})
        elif (state == 1):
            y -= 1
            postionlist.append({'x': x, 'y': y})
        elif (state == 2):
            x += 1
            postionlist.append({'x': x, 'y': y})
        elif (state == 3):
            y += 1
            postionlist.append({'x': x, 'y': y})

for i in range(len(postionlist)):
    xlist.append(postionlist[i]['x'])
    ylist.append(postionlist[i]['y'])

minvalue = abs(min(ylist))
minxvalue = abs(min(xlist))
col = abs(min(xlist)) + abs(max(xlist)) + 1
row = abs(min(ylist))+abs(max(ylist)) + 1
array = [['#']*col for i in range(row)]

for i in range(len(postionlist)):
    array[postionlist[i]['y']+minvalue][postionlist[i]['x']+minxvalue] = '.'

for i in array:
    for j in i:
        print(j, end="")
    print()
