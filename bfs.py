def bfs(graph, start, target):
    visited = []
    visited.append(start)
    queue = []
    queue.append(start)

    while queue:
        m = queue.pop(0)
        if m == target:
            return m
        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
                if neighbor == target:
                    return visited
    return 'Item not in List!'
    

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
    bfs_traversal = bfs(graph, start, target)

    print('Path:', *bfs_traversal, sep=" -> ")
    print(f'Path Cost => {len(bfs_traversal)}')


if __name__ == '__main__':
    main()
