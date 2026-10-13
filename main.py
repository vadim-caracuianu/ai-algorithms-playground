#from search.bfs import bfs
#from search.dfs import dfs
#from search.ucs import ucs
from search.greedy import greedy

#For bfs, dfs, greedy only
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

#path = bfs(graph, "A", "F")
#path = dfs(graph, "A", "F")

#For ucs only
#weighted_graph = {
#     "A": [("B", 4), ("C", 2)],
#     "B": [("D", 5)],
#     "C": [("E", 3)],
#     "D": [("F", 2)],
#     "E": [("F", 1)],
#     "F": []
# }

#path = ucs(weighted_graph, "A", "F")

heuristic = {
    "A": 6,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}

path = greedy(graph, heuristic, "A", "F")
print(path)

