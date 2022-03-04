def shortest_path(graph, start,end):
    visited = [start]
    queue = [start]
    count = -1

    while queue:
        count += 1

        size = len(queue)

        for i in range(size):
            n = queue.pop(0)

            if n == end:
                return count
            
            for next in graph[n]:
                if next not in visited:
                    visited.append(next)
                    queue.append(next)

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(shortest_path(graph, 'A', 'F'))