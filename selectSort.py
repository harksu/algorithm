from cgitb import small


def findSmallest(list):
    smallest = list[0]
    smallestIndex = 0
    for i in range(len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallestIndex = i
    return smallestIndex


def selectionSort(list):
    newList = []
    for i in range (len(list)):
        smallest = findSmallest(list)
        newList.append(list.pop(smallest))
    return newList

tempList = [5,3,6,2,10,1,-2,3,-5]
print(selectionSort(tempList))