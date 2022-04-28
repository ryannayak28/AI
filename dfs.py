def dfs(graph, start, target, path, visited=list()):
    path.append(start)
    visited.append(start)
    if start == target:
        return path
    for neighbour in graph[start]:
        if neighbour not in visited:
            if neighbour == target:
                visited.append(neighbour)
                return visited
            result = dfs(graph, neighbour, target, path, visited)
            if result is not None:
                return result
    path.pop()
    return None


def main():
    graph = {
        'A' : ['B', 'C', 'D'],
        'B' : ['A', 'E', 'F'],
        'C' : ['A', 'F'],
        'D' : ['A'],
        'E' : ['B'],
        'F' : ['B', 'C']
    }
    start = input("Enter Start Node: ")
    target = input("Enter Target Node: ")
    dfs_traversal = []
    dfs_traversal = dfs(graph, start, target, dfs_traversal)

    print('Path:', *dfs_traversal, sep=" -> ")
    print(f'Path Cost => {len(dfs_traversal)}')


if __name__ == '__main__':
    main()

