from search.bfs import bfs


graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

path = bfs(graph, "A", "F")

print(path)

