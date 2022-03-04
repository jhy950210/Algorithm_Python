def bfs(graph, start):
    visited = []
    queue =[start]

    while queue:
        n = queue.pop(0)

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    
    return visited