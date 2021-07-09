# Uses python3
import sys

def merge(a, b, left, right):
    inv = 0
    l = left
    c = left
    ave = (left + right) // 2
    r = ave + 1

    while l <= ave and r <= (right):
        if a[l] <= a[r]:
            b[c] = a[l]
            l += 1
            c += 1
        else:
            b[c] = a[r]
            r += 1
            c += 1
            inv += (ave - l + 1)

    while l <= ave:

        b[c] = a[l]
        c += 1
        l += 1

    while r <= (right):
        b[c] = a[r]
        c += 1
        r += 1

    for i in range(left, (right+1)):
        a[i] = b[i]
    return inv

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if left >= right:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave+ 1, right)
    #write your code here
    number_of_inversions += merge(a, b, left, right)


    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))
