# Uses python3
import sys

def get_change(m):
    #write your code here
    minimum(0)
    list = (m+1)*[0]
    list[0] = 0

    for i in range(1, m+1):
        if i >= 3:
            if list[i-1] <= list[i-3] and list[i-1] <= list[i-4]:
                list[i] = list[i-1] + 1

            elif list[i-3] <= list[i-1] and list[i-3] <= list[i-4]:
                list[i] = list[i-3] + 1


            elif list[i-4] <= list[i-1] and list[i-4] <= list[i-3]:

                list[i] = list[i - 4] + 1

        else:
            list[i] = i

    return list[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
