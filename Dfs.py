#Depth first search

#솔직히 할거 많아서 탐색 알고리즘은 제대로 못한 느낌이 강하니까 다녀와서 제대로 하기
graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

from collections import deque

def Dfs(graph, strat_node):
    visited = []
    search_queue = deque()

    search_queue.append(strat_node)
    
    while search_queue:
        node = search_queue.popleft()
        if node not in visited:
            
            visited.append(node)
            search_queue.extend(graph[node])
            
    return visited

Dfs(graph, 'A')