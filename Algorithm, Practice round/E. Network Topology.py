pair_count = int(input())
pairs = []
for pair_index in range(pair_count):
    pairs.append([int(node) - 1 for node in input().split()])

node_count = pair_count + 1
matrix = [[0]*node_count for i in range(node_count)]

for pair in pairs:
    print(pair)
    first, second = int(pair[0]), int(pair[1])
    matrix[first][second] = matrix[second][first] = 1
print(matrix)


def get_distance(matrix, v, h):
    print(list(filter(lambda x: x > 0, sorted(matrix[v]))))
    for min_i in list(filter(lambda x: x > 0, sorted(matrix[v]))):
        for i in range(h + 1):
            if matrix[v][i] >= min_i:
                if matrix[i][h] >= 1:
                    return matrix[v][i] + matrix[i][h]
                return matrix[v][i] + get_distance(matrix, i, h)
    return -1


for i in range(pair_count):
    for j in range(pair_count):
        if matrix[i][j] == 0 and i != j:
            matrix[i][j] = matrix[j][i] = get_distance(matrix, i, j)
[print(matrix[i]) for i in range(node_count)]