#from search.bfs import bfs
from search.dfs import dfs

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

#path = bfs(graph, "A", "F")
path = dfs(graph, "A", "F")

print(path)

