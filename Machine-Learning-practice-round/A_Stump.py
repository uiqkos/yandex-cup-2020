import math
import numpy as np

def mse(predicted, excepted):
    return np.sum((predicted - excepted) ** 2) / (2 * len(predicted))

def smse(predicted, expected):
    return np.sqrt(np.sum((predicted - expected) ** 2) / (2 * len(predicted))

def stump(pairs):
    pairs.sort(key=lambda pair: pair[0])
    X = np.array(list(map(lambda tup: tup[0], pairs)))
    Y = np.array(list(map(lambda tup: tup[1], pairs)))

    left, right = [], Y.copy()
    left_sum = 0
    right_sum = sum(right)

    c = Y[0]
    a, b = Y[0], right_sum / len(right)
    # best = (a, b, c, smse(np.array([b]*len(right)), Y), mse(np.array([b]*len(right)), Y))
    best = (a, b, c, smse(np.array([b]*len(right)), Y))

    for border in range(len(X)):
        left.append(Y[border])
        right = np.delete(right, 0)

        left_sum += Y[border]
        right_sum -= Y[border]

        a = left_sum / len(left)
        # a = 0.002 * (left_sum / len(left)) + 4.38987855 * len(pairs)
        b = right_sum / len(right) if len(right) > 0 else Y[-1]
        # b = 0.002 * (right_sum / len(right)) + 4.38987855 * len(pairs) if len(right) > 0 else Y[-1]
        # mse_error = mse(np.array([a] * len(left) + [b] * len(right)), Y)
        smse_error = smse(np.array([a] * len(left) + [b] * len(right)), Y)

        if border == len(X) - 1:
            c = X[-1]
        else:
            c = (X[border + 1] + X[border]) / 2

        if best[3] > smse_error:
            best = (a, b, c, smse_error)

    # if best[3] < error:
    a, b, c, smse_error = best

    if __name__ == '__main__':
        return f'{a:.6f} {b:.6f} {c:.6f}'

    return a, b, c, smse_error

if __name__ == '__main__':
    pair_count = int(input())
    pairs = [[float(num) for num in input().split()] for i in range(pair_count)]
    print(stump(pairs))