#NOTE - a tree wouldn't need to check for "visited" states
#       because you can't climb back up the branches
#       or better said: it doesn't have cycles

#graaph manually assigned as a dictionary
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

start = "A"
goal = "F"

frontier = [start]
visited = {start}

#implementing a dictionary to remember how we reached each node
parent = {start: None}


#checks the frontier for neighbors
while frontier:
    current = frontier.pop(0)
    print(current)
   
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            parent[neighbor] = current #this fills the parent dictionary, so every node has a parent
            frontier.append(neighbor)

path = []
current = goal

#we found the goal state, and we are adding every parent to the path
while current is not None:
    path.append(current)
    current = parent[current]

path.reverse()

print(path)

