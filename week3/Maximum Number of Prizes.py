# Uses python3
import sys

def optimal_summands(n):
    summands = []
    k = 1
    rest = n
    while rest != 0:
        rest -= k

        if rest > k:
            summands.append(k)
            k += 1
        elif rest <= k:
            k += rest
            summands.append(k)
            rest = 0



    #write your code here
    return summands

if __name__ == '__main__':
    x = int(input())
    n = x
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
