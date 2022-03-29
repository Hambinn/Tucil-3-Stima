import random

def randomList():
    list = random.sample(range(1, 17), 16)
    print(list)

    puzzle = [[0 for a in range(4)] for b in range(4)]
    for i in range(4):
        for j in range(4):
            if(list[i*4+j] == 16):
                puzzle[i][j] = 0
            else:
                puzzle[i][j] = list[i*4+j]

    print(puzzle)
    return puzzle

def totalKurang(puzzle,a,i,j):
    sum = 0
    for b in range(i,4):
        for c in range(j,4):
            if(a > puzzle[b][c] and puzzle[b][c] != 0):
                print(a, " ", puzzle[b][c])
                sum += 1
            else:
                sum += 0
    return sum
                

def kurangi(puzzle):
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += totalKurang(puzzle,puzzle[i][j],i,j)
    return sum

print(kurangi(randomList()))

