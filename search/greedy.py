#UCS prioritizes accumulated cost. Greedy prioritizes the estimated distance to the goal (heuristic).

import heapq

def greedy(graph, heuristic, start, goal):
    frontier = [(heuristic[start], start)]
    parent = {start: None}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in parent:
                parent[neighbor] = current
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path 



