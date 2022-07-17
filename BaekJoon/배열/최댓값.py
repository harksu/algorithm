list = []

for i in range(1,10):
    list.append(int(input()))
print(max(list))
count = list.index(max(list))
print(count + 1)