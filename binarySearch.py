

def mySolt(list): #탐색 하기 전에 일단 정렬 
    listLength = len(list)-1 # 반복문을 위한 배열문 길이 저장(비교를 해야하므로 1을 제외) => 배열의 인덱스에 접근할 땐 1을 빼고, 단순 출력 반복문이면 그냥 돌리고 
    for j in range (listLength): # 완전 정렬을 위해서 2중 for문
        for i in range (listLength):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i]=list[i+1]
                list[i+1] = temp
    return list #그리고 정렬 된 리스트를 반환 
    
    
def showList(list):
        listLength = len(list)
        for i in range (listLength):
            print(list[i],end=' ')
   
    
def binarySearch(list, item):
    low = 0  # 초기값은 일단 0번째 인덱스 
    high = len(list)-1 # 가장 높은 인덱스는 해당 식 
   
    
    
    while(low <= high):  # 탐색이니까 당연히 최하 인덱스와 최상 인덱스가 동일될 때 까지 
        mid = (low + high) // 2 # 중앙값 설정 
        guess = list[mid] # 추측값은 무조건 가운데로 
        if item == guess: # 만약 맞춘다면 가운데에 있는 인덱스를 반환(애초에 탐색 이니까 위치를 찾는 것이므로)
            return mid
        if guess > item: # 만약 추측값이 더 크다면 범위를 위에서 줄여야됨(더 큰 것이 필요가 없으니까 )
            high = mid - 1
        else:
            low = mid + 1 # 만약 추측값이 더 작다면 범위를 밑에서 줄여야됨(더 작은 것이 필요가 없으니까 )
    return None # 이거 들여쓰기 때문에 어리버리 깠는데, 애초에 해당 리스트에 없으면 None 반환 
    
mylist = [1,3,5,7,9]

showList(mySolt(mylist)) 
    