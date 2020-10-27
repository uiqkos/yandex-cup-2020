## Get data
n, m = [int(i) for i in input().split()]
A, B = [int(a) for a in input().split()], [int(b) for b in input().split()]

def get_range(h, v):
    if isinstance(v, tuple):  # Get vertical line
        return [A[i] * 10**9 + B[h] for i in range(*v)]

    if isinstance(h, tuple):  # Get horizontal line
        return [A[v] * 10**9 + B[j] for j in range(*h)]

    return A[v] * 10**9 + B[h]


max_a, max_b = max(A), max(B)

A_indexes = list(filter(lambda i: A[i] == max_a, range(n)))
B_indexes = list(filter(lambda j: B[j] == max_b, range(m)))

A_index = B_index = i = j = res = 0
while True:
    # If at max a and max b
    if B_index >= len(B_indexes) and A_index >= len(A_indexes):
        res += sum(get_range((j, m - 1), i))
        res += sum(get_range(m - 1, (i, n - 1)))
        res += get_range(-1, -1)
        break

    # Go to max a
    if A_index < len(A_indexes):
        res += sum(get_range(j, (i, A_indexes[A_index])))
        i = A_indexes[A_index]
        A_index += 1

    # Go to max b
    if B_index < len(B_indexes):
        res += sum(get_range((j, B_indexes[B_index]), i))
        j = B_indexes[B_index]
        B_index += 1

print(res)

# ### Dynamic
# matrix = []
# for i in range(0, len(A)):
#     matrix.append([])
#     for j in range(0, len(B)):
#         matrix[i].append(max(
#             matrix[i - 1][j] if i > 0 else 0,
#             matrix[i][j - 1] if j > 0 else 0
#         ) + A[i] * 10 ** 9 + B[j])
#
# print(matrix[-1][-1])
