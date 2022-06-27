from cgitb import small


def findSmallest(list):
    smallest = list[0] #일단 최소값을 설정 
    smallestIndex = 0
    for i in range(len(list)): #배열 길이만큼 반복문을 돌려서 
        if list[i] < smallest:
            smallest = list[i]
            smallestIndex = i # 최소값에 해당하는 인덱스를 찾아서 
    return smallestIndex #반환 , 내가 아는 알고리즘이랑 같은데 코드가 다르니까 일단 알아두기 


def selectionSort(list):
    newList = [] # 새로운 리스트를 생성해서 반환 하는 형식 
    for i in range (len(list)):
        smallest = findSmallest(list)
        newList.append(list.pop(smallest)) # 그리고 새로운 리스트에서 값을 넣어주는 동시에, 기존의 리스트에서 값을 빼오면서 메모리를 관리 
    return newList #그리고 마지막에 리스트를 리턴해줘야함 

tempList = [5,3,6,2,10,1,-2,3,-5]
print(selectionSort(tempList))