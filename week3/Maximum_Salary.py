# Uses python3

import sys

def IsGreaterOrEqual(digit, maxdigit):
    if int(digit + maxdigit) > int(maxdigit + digit):
        return digit
    else:
        return maxdigit

def largest_number(a):
    # write your code here
    res = ""
    maximum = a[0]

    while len(a) > 0:
        for x in a:
            maximum = IsGreaterOrEqual(x, maximum)

        res += (str(maximum))
        a.remove(maximum)
        maximum = '0'
            # print(a)
    return res



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

