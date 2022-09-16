# n = int(input())
# beforelist = []
# for i in range(n):
#     text = input()
#     beforelist.append(text)

# itemlist =list(set(beforelist)) #이건 숙지하기
# itemlist.sort()
# count = len(itemlist)-1
# for j in range(count):    
#     for i in range(count):
#         if(len(itemlist[i])>len(itemlist[i+1])):
#             temp = itemlist[i]
#             itemlist[i] = itemlist[i+1]
#             itemlist[i+1] = temp
#         # elif(len(itemlist[i])==len(itemlist[i+1])): 이 조건문은 애초에 필요가 없음, 그냥 사전으로 먼저 솔팅하고 그 다음에 길이로 솔팅하면 되니까 
          
# for i in itemlist:
#     print(i)
    
    
#이건 아쉽게도 시간 초과 났던 알고리즘이므로, 다른 방법 구글링해서 해결 



N = int(input())
text = []

for i in range(N):
    text.append(input())
set_text = set(text)
text = list(set_text)

text.sort()
text.sort(key=len) #이런 메소드가 있는걸 몰랐음 
for i in range(len(text)):
    print(text[i])
