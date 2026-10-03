def bfs(graph, start, goal):
    frontier = [start]
    visited = {start}
    parent = {start: None}

    while frontier:
        current = frontier.pop(0)

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

