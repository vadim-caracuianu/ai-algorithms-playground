import heapq

def astar(graph, heuristic, start, goal):
    frontier = [(heuristic[start], start)]
    parent = {start: None}
    cost = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor, edge_cost in graph[current]:
            new_cost = cost[current] + edge_cost 

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))
    
    path = []
    current = goal 

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path
