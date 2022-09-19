
def func(count):
    item = [1, 1]
    if (count == 0):
        one = 0
        zero = 1
        print(zero, one, end=' ')
        print()
        return
    if (count == 1):
        one = 1
        zero = 0
        print(zero, one, end=' ')
        print()
        return
    for i in range(count):
        if (i == 0 or i == 1):
            pass
        else:
            item.append(item[i-1]+item[i-2])
    print(item[i-1], item[i], end=' ')
    print()


t = int(input())
testset = []
for i in range(t):
    testset.append(int(input()))
for j in testset:
    func(j)
