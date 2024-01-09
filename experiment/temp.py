t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    map = []
    counter = 0

    for i in range(n):
        map.append(list(input()))

    # check te corners
    if map[0][0] == "O":
        if map[1][0] == "X" and map[0][1] == "X" and map[1][1] == "X":
            counter += 1
    if map[0][m-1] == "O":
        if map[1][m-1] == "X" and map[0][m-2] == "X" and map[1][m-2] == "X":
            counter += 1
    if map[n-1][0] == "O":
        if map[n-1][1] == "X" and map[n-2][1] == "X" and map[n-2][0] == "X":
            counter += 1
    if map[n-1][m-1] == "O":
        if map[n-2][m-1] == "X" and map[n-2][m-2] == "X" and map[n-1][m-2] == "X":
            counter += 1

    # check the border rows and columns (don't check the corners again)
    for i in range(1, m-1):
        if map[0][i] == "O":


    for i in range(1,n-1):
        for j in range(1,m-1):
            baseable = False
            if map[i][j] == "O":
                baseable = True
                for k in range(-1,2):
                    if map[i-1][j+k] != "X":
                        baseable = False
                        break
                    if map[i+1][j+k] != "X":
                        baseable = False
                        break
                    if map[i][j-1] != "X" or map[i][j+1] != "X":
                        baseable = False
                        break
            if baseable:
                counter += 1

    print(counter)