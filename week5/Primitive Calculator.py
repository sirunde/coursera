# Uses python3
import sys

def get_change(m):
    #write your code here
    list = (m+1)*[0]
    list[1] = 0

    for i in range(2, m+1):

        if i % 3 == 0:
            if i % 2 == 0:
                if list[i//3] <= list[i-1] and list[i//3] <= list[i//2]:
                    list[i] += list[i//3] + 1
                else:
                    list[i] += list[i-1] + 1
            else:
                if list[i//3] <= list[i-1]:
                    list[i] += list[i//3] + 1
                else:
                    list[i] += list[i-1] + 1
        elif i % 2 == 0:
            if list[i//2] <= list[i-1]:
                list[i] += list[i//2] + 1
            else:
                list[i] += list[i-1] + 1

        else:
            list[i] += list[i-1] + 1

    return list


def sequen(n):
    list = get_change(n)
    hop = []
    hop.append(n)
    while n != 1:
        if n % 3 == 0:
            if n % 2 == 0:
                if list[n // 3] <= list[n - 1] and list[n // 3] <= list[n // 2]:
                    hop.append(n//3)
                    n = n//3

                else:
                    hop.append(n-1)
                    n = n - 1

            else:
                if list[n // 3] <= list[n - 1]:
                    hop.append(n//3)
                    n = n//3

                else:
                    hop.append(n-1)
                    n = n-1

        elif n % 2 == 0:
            if list[n // 2] <= list[n - 1]:
                hop.append(n//2)
                n = n // 2

            else:
                hop.append(n-1)
                n -= 1

        else:
            hop.append(n-1)
            n -= 1

    return reversed(hop)


if __name__ == "__main__":

    input = sys.stdin.read()
    n = int(input)
    sequence = list(sequen(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
