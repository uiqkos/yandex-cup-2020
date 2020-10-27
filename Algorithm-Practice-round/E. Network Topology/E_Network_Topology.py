# from .E_Network_Topology_iterate import fill_matrix as fill_matrix_iterate

# fill_matrix_iterate = __import__(
#     'E_Network_Topology_iterate',
#     fromlist=['fill_matrix']
# ).fill_matrix

def get_distance(matrix, from_, to_, exclude=[]):
    if matrix[from_][to_] > 0:
        return matrix[from_][to_]

    path_len = len(matrix) - len(exclude)
    for through_ in range(len(matrix)):
        if matrix[from_][through_] > 0 and through_ not in exclude:
            path_len = min(
                path_len,
                matrix[from_][through_] + get_distance(matrix, through_, to_, exclude=exclude + [from_])
            )
    return path_len

def fill_matrix(edges, node_count=None):
    if node_count is None:
        node_count = len(edges) + 1

    matrix = [[0] * node_count for i in range(node_count)]

    for pair in edges:
        first, second = int(pair[0]) - 1, int(pair[1]) - 1
        matrix[first][second] = matrix[second][first] = 1

    for i in range(node_count):
        for j in range(node_count):
            if matrix[i][j] == 0 and i != j:
                matrix[i][j] = matrix[j][i] = get_distance(matrix, i, j)

    return matrix

def fill_matrix_iterate(edges):
    node_count = len(edges) + 1
    matrix = [[0] * node_count for i in range(node_count)]  # [node1][node2]: len(path(node1, node2))
    nodes = []  # node_1, node_2, ..., node_n

    for pair_index, pair in enumerate(edges):
        node1, node2 = int(pair[0]) - 1, int(pair[1]) - 1
        matrix[node1][node2] = matrix[node2][node1] = 1
        if len(nodes) == 0:
            nodes.append(node1)

        new_node, old_node = (node1, node2) if node1 not in nodes else (node2, node1)

        for node in nodes:
            if node != node1 != node2:
                matrix[new_node][node] = matrix[node][new_node] = matrix[node][old_node] + 1

        nodes.append(new_node)
    return matrix

def get_best_nodes(node_count, edges, iterate=False):
    if isinstance(edges, str):
        edges = [[int(n) for n in pair.split()] for pair in edges.split('\n' if '\n' in edges else '; ')]

    if iterate:
        matrix = fill_matrix_iterate(edges)
    else:
        matrix = fill_matrix(edges)

    maybe = {}
    for first in range(node_count):
        for second in range(node_count):
            if first != second:
                maybe[(first + 1, second + 1)] = \
                    sum([
                        min(matrix[first][node], matrix[second][node])
                        for node in range(node_count)
                    ])
    # maybe = sorted(maybe.items(), key=lambda tup: tup[1])
    return min(maybe.items(), key=lambda tup: tup[1])[0]


if __name__ == '__main__':
    node_count_ = int(input())
    pairs = []
    for i in range(node_count_ - 1):
        pairs.append([int(node) for node in input().split()])
    # print(*get_best_nodes(9, '1 2; 2 3; 2 5; 4 5; 6 5; 5 7; 7 8; 7 9'))
    print(*get_best_nodes(node_count_, pairs, iterate=False))
