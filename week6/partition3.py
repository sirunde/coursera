# Uses python3
import sys
import itertools

def partiton(A, B = 3):
    total = sum(A)
    rem = total%B
    third = total//B

    if rem > 0 or max(A) > third or len(A) < B :
        return 0
    A = [0]+ A
    matrix = [[0 for i in range(len(A))] for j in range(third+1)]
    memory = [[0 for i in range(len(A))] for j in range(third+1)]


    for i in range(1, len(A)):
        for j in range(1, third+1):

            matrix[j][i] = matrix[j][i - 1]
            memory[j][i] = memory[j][i-1]
            if A[i] <= j:
                val = matrix[j - A[i]][i - 1] + A[i]

                if matrix[j][i] < val:
                    a = []
                    b = memory[j-A[i]][i-1]
                    if b == 0:
                        a.append(b)
                    else:
                        a.extend(b)
                    a.append(A[i])
                    memory[j][i] = a
                    matrix[j][i] = val
                if matrix[j][i] == third:
                    for i in (memory[j][i]):
                        A.remove(i)
                    break

        else:
            continue
        break

    if matrix[-1][-1] != third and matrix[-1][-1] != 0:
        return 0

    else:
        if B > 1:

            B -= 1
            partiton(A, B)

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partiton(A))
    # print(partition3(A))

