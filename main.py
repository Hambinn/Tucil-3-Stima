import random

list = random.sample(range(1, 17), 16)
def randomList():
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

def totalKurang(list,a,i,j):
    sum = 0
    for b in range((i*4+j),len(list)):
        print("masuk")
        print(list)
        if(a > list[b] and list[b] != 0):
            print(a, " ", list[b])
            sum += 1
        else:
            sum += 0
    return sum
                

def kurangi(puzzle):
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += totalKurang(list,puzzle[i][j],i,j)
    return sum

print(kurangi(randomList()))

