# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x, j, t = a[l], l, r
    i = j

    while i <= t:
        if a[i] < x:
            a[j], a[i] = a[i], a[j]
            j += 1
            i += 1

        elif a[i] > x:
            a[t], a[i] = a[i], a[t]
            t -= 1

        else:
            i += 1
    return j, t

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3

    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)  # left
    randomized_quick_sort(a, n + 1, r)  # right

def stresstest():
    a = []
    n = random.randint(1, 100000)
    for i in range(n):
        i = random.randint(1, 100000)
        a.append(i)
    b = sorted(a)
    randomized_quick_sort(a, 0, n-1)
    print(a)
    print(b)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
