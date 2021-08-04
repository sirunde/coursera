# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w = [0] + w
    item = len(w)
    cap = W + 1

    weights = [[0 for i in range(item)] for j in range(cap)]

    for i in range(1, item):
        for j in range(1, cap):
            weights[j][i] = weights[j][i - 1]
            if w[i] <= j:
                val = weights[j - w[i]][i - 1] + w[i]
                if weights[j][i] < val:
                    weights[j][i] = val

    return weights[-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
