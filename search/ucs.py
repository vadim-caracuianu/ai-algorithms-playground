#UCS -> lowest total edge cost
#it sacrifices exploration efficiency for guaranteed omptimality when the goal is found

#python built in min-heap
import heapq

def ucs(graph, start, goal):
    # (cost, node)
    frontier = [(0, start)]
    parent = {start: None}
    cost = {start: 0}

    while frontier:
        current_cost, current = heapq.heappop(frontier)

        if current == goal:
            break

        #examines the current node's neighbors
        for neighbor, edge_cost in graph[current]:
            new_cost = current_cost + edge_cost 

            #updates cost, parent, frontier if this route is new or cheaper
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(frontier, (new_cost, neighbor))
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()
    return path
