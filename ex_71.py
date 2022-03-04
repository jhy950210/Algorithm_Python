from turtle import st


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()

        print('stack:',stack)

        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    
    return visited

graph = {
        'A': set(['B', 'C', 'E']),
        'B': set(['A']),
        'C': set(['A']),
        'D': set(['E', 'F']),
        'E': set(['A', 'D']),
        'F': set(['D'])
}

print(dfs(graph, 'E'))