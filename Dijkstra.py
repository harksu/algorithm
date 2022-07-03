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
    lowest_cost_node = None
    for node in cost:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node