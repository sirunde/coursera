# Uses python3
import sys

def get_majority_element(a, left, right):

    if left == right:
        return -1

    if left + 1 == right:
        return a[left]

    mid = (left + right) // 2


    l = get_majority_element(a, left, mid)
    r = get_majority_element(a, mid, right)

    els = (a for a in (l, r) if a != -1)
    for el in els:
        cnt = 0
        for i in range(left, right):
            if a[i] == el:
                cnt += 1
        if cnt > (right - left) / 2:
            return el

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
