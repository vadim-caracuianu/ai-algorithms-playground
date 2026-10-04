#DFS -> LIFO -> explores deep -> does not guarantee shortest path

def dfs(graph, start, goal):
    frontier = [start]
    visited = {start}
    parent = {start: None}

    while frontier:
        current = frontier.pop()
        
        if current == goal:
            break

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor) 
                parent[neighbor] = current 
                frontier.append(neighbor)
    
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path
