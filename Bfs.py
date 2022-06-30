#너비 우선 탐색 
#아 나도 개인 공부 위주로 좀 공부하고 싶다 ㅠ


from collections import deque

def isAnswer(item,answer):
    return item == answer
    

def bfs(graph,item,answer):
    search_queue = deque()
    search_queue += (graph[item])
    visited = []
    while search_queue:
        findValue = search_queue.popleft()
        if not findValue in visited:
            if isAnswer(findValue,answer):
                print("찾았습니다")
                return True
        else:
            search_queue += (graph[findValue])
            visited.append(findValue)
    print("못 찾았습니다")            
    return False

temp = {
    "you":["a","b","c","x"]
}

bfs(temp,"you","x")

#알고리즘 로직 공부하기 새벽이라 머리가 안돌아간다 