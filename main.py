#from search.bfs import bfs
#from search.dfs import dfs
from search.ucs import ucs

#For bfs and dfs only
#graph = {
    #"A": ["B", "C"],
    #"B": ["D"],
    #"C": ["E"],
    #"D": ["F"],
    #"E": ["F"],
    #"F": []
#}

#path = bfs(graph, "A", "F")
#path = dfs(graph, "A", "F")

#For ucs only
weighted_graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5)],
    "C": [("E", 3)],
    "D": [("F", 2)],
    "E": [("F", 1)],
    "F": []
}

path = ucs(weighted_graph, "A", "F")
print(path)

