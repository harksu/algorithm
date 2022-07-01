#Depth first search

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
        print(node, end = " ")
        if node not in visited:
            
            visited.append(node)
            search_queue.extend(graph[node])
            
    return visited

Dfs(graph, 'A')