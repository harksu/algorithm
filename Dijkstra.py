# 다익스트라 알고리즘 

graph = {}
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"]={}
graph["b"]["a"]=3
graph["b"]["fin"]=5
graph["fin"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None 

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None #일단 초기 설정은 다 처음으로 잡고 
    for node in costs: # 노드를 돌리는데 
        cost = costs[node] #차례에 해당하는 노드에 대한 비용이 
        if cost < lowest_cost and node not in processed: # 만약 더 싸고, 아직 들린 곳이 아니였다면 
            lowest_cost = cost
            lowest_cost_node = node #갱신 
    return lowest_cost_node # 반복문 끝나고 남은 노드를 반환 


def dijkstra(costs):
    node = find_lowest_cost_node(costs) #일단 가장 싼 노드를 결정하고 
    while node is not None: # 그 노드에 대해서 반복문을 돌리는데 
        cost = costs[node]  #차례에 해당하는 노드에 대한 비용
        neighbors = graph[node] #이웃 노드
        for n in neighbors.keys(): #이웃에 대해서 반복문을 돌림 
            new_cost = cost + neighbors[n] # 새로운 비용은 기존의 비용과 이웃의 차례에 해당하는 비용을 더함(모든 경우의 수를 판단해야 하므로)
            if(costs[n] > new_cost): # 만약 새로운 정점을 지나는 것이 더 싸다면 
                costs[n] = new_cost #갱신 
                parents[n] = node #부모를 이 정점으로 갱신 
        processed.append(node) #처리한 사실 기록 
        node = find_lowest_cost_node(costs) # 다음으로 처리할 정점을 찾아 반복 