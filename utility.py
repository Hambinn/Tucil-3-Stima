import random
listRandom = random.sample(range(1, 17), 16)

def readfile(fileName):
    array = []
    with open(fileName, 'r') as file:
        for line in file:
            line.split(" ")
            strings = parseString(line.split())
            array += strings
    return array

def parseString(strings):
    for i in range(len(strings)):
        strings[i] = int(strings[i])
    return strings

def listToMatrix(array):
    puzzle = [[0 for a in range(4)] for b in range(4)]
    for i in range(4):
        for j in range(4):
            puzzle[i][j] = array[i*4+j]
    return puzzle

def totalKurang(list,a,i,j):
    sum = 0
    for b in range((i*4+j),len(list)):
        if(a > list[b] and list[b] != 0):
            sum += 1
        else:
            sum += 0
    return sum

def kurangi(puzzle,array): 
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += totalKurang(array,puzzle[i][j],i,j)
    posisikosong = posisiKosong(puzzle)
    return sum + posisikosong

def posisiKosong(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                if((i+j) % 2 == 0):
                    return 0
                else:
                    return 1

def countG(puzzle):
    count = 0
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] != 16 and puzzle[i][j] != i*4+j+1):
                print(puzzle[i][j])
                count += 1
    return count

def moveUp(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                if(i-1 >= 0):
                    puzzle[i][j] = puzzle[i-1][j]
                    puzzle[i-1][j] = 16
                    return puzzle

def moveDown(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                if(i+1 < 4):
                    puzzle[i][j] = puzzle[i+1][j]
                    puzzle[i+1][j] = 16
                    return puzzle

def moveLeft(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                if(j-1 >= 0):
                    puzzle[i][j] = puzzle[i][j-1]
                    puzzle[i][j-1] = 16
                    return puzzle

def moveRight(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                if(j+1 < 4):
                    puzzle[i][j] = puzzle[i][j+1]
                    puzzle[i][j+1] = 16
                    return puzzle

def printPuzzle(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                print("  ", end="")
            else:
                print(puzzle[i][j],end=" ")                
        print()

def generateBranch(puzzle,branch):
    branch.append(puzzle)
    branch.append(moveUp(puzzle))
    branch.append(moveDown(puzzle))
    branch.append(moveLeft(puzzle))
    branch.append(moveRight(puzzle))