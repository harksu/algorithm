#너비 우선 탐색 
#아 나도 개인 공부 위주로 좀 공부하고 싶다 ㅠ


from collections import deque

def isAnswer(item,answer):
    return item == answer
    

def bfs(graph,item,answer):
    search_queue = deque() # 일단 큐의 형태로 관리를 하는데 
    search_queue += (graph[item]) # 그래프의 키 값을 하나 땡겨와서 
    visited = [] # 이건 방문 한 노드들 따로 빼놓는 리스트고 
    while search_queue:  # 큐가 없어질 때 까지 
        findValue = search_queue.popleft() # 현재 비교하는 값은 큐에서 하나를 뺀 값이고 
        if not findValue in visited: # 만약 그 값이 방문하지 않은 노드라면 
            if isAnswer(findValue,answer): # 해당 조건문을 연산하는데, 내가 찾는 값과 동일하다면 
                print("찾았습니다")
                return True # 참 반환 
        else:
            search_queue += (graph[findValue]) # 근데 아니라면, 큐에다가 다시 넣는거임
            visited.append(findValue) # 그리고 그 값은 방문한 노드니까 리스트로 따로 관리하고
    print("못 찾았습니다")            
    return False

temp = {
    "youd":["a","b","c","f"],
    "youu":["a","b","c","z"],
    "youy":["a","b","c","y"],
    "you":["a","b","c","x"]
}

bfs(temp,"you","x")

#알고리즘 로직 공부하기 새벽이라 머리가 안돌아간다 