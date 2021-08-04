# Uses python3
def edit_distance(s, t):
    #write your icode here
    list= [0]*(len(s)+1)

    for i in range(len(s)+1):
        list[i] = [0]*(len(t)+1)

    for i in range(1, (len(s)+1)):
        list[i][0] = i
    for j in range(1,len(t)+1):
        list[0][j] = j

    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            insert = list[i][j-1] + 1
            delete = list[i-1][j] + 1
            match = list[i-1][j-1]
            dismatch = list[i-1][j-1] + 1
            if s[i-1] == t[j-1]:
                list[i][j] = min(insert,delete,match)
            else:
                list[i][j] = min(insert, delete, dismatch)

    return list[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
