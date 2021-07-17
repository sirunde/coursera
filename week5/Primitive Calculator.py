# Uses python3
import sys

def get_change(m):
    #write your code here
    list = (m+1)*[0]
    list[1] = 0

    for i in range(2, m+1):
        if i%2 == 0:
            if i%3 ==0:
                if list[i - 1] <= list[i // 2] and list[i-1] <= list[i//3]:
                    list[i] += list[i - 1] + 1
                elif list[i//3] <= list[i//2] and list[i//3] <= list[i-1]:
                    list[i] += list[i//3] + 1

                else:
                    list[i] += list[i//2]+1
            else:

                if list[i - 1] <= list[i // 2]:
                    list[i] += list[i - 1] + 1

                else:
                    list[i] += list[i // 2] + 1

        elif i%3 == 0:
            if i%2 == 0:
                if list[i-1] <= list[i//3] and list[i-1] <= list[i//2]:
                    list[i] += list[i-1]+1
                elif list[i//2] <= list[i-1] and list[i//2] <= list[i//3]:
                    list[i] += list[i//2]

                else:
                    list[i] += list[i//3]

            else:
                if list[i-1] <= list[i//3]:
                    list[i] += list[i-1]

                else:
                    list[i] 

    return list[m]


def sequen(n):
    hop_count= [0]*(n+1)
    hop_count[1] = 1
    for i in range(2, n + 1):
        indices = [i - 1]
        if i % 2 == 0:
            indices.append(i // 2)
        if i % 3 == 0:
            indices.append(i // 3)

        # Get the index with the least hop count to 1.
        min_hops = min([hop_count[x] for x in indices])

        # Write hop count from current index to 1. Hop count incremented by 1.
        hop_count[i] = min_hops + 1

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:

            n = n // 3

        elif n % 2 == 0:

            if (n-1)% 3 == 0:
                n -= 1

            else:
                n = n // 2

        else:
            n = n - 1

    return reversed(sequence)

if __name__ == "__main__":
    sequen(5)
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
