#퀵정렬

def quickSort(list): 
    if(len(list)<2): #만약 리스트의 길이가 2도 안된다면 애초에 정렬을 할 필요가 x
        return list
    standard = list[0] #기준점을 0번째 인덱스로 접근하고 
    lessPart,equalPart,greatePart = [],[],[] # 세 가지의 케이스 배열이 있으므로, 세가지 리스트 선언 
    for number in list: # 리스트 반복문을 돌려서 세 개의 리스트로 나눔
        if number < standard:
            lessPart.append(number)
        elif number > standard:
            greatePart.append(number)
        else:
            equalPart.append(number)
   
    return quickSort(lessPart) + equalPart + quickSort(greatePart) #나눠진 세개의 리스트는 재귀적으로 정렬하여서 반환

print (quickSort([1,100,10,5,2,2,2,3]))