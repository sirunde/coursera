# Uses python3
import sys

def sequen(n):
    list = [0]*(n+1)
    list[0] = 0
    output = []
    output.append(1)

    for i in range (n, 0, -1):
        pass

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:

            if (n-1)% 3 == 0:
                n -= 1

            else:
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

    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
