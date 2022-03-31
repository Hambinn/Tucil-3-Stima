import random
listRandom = random.sample(range(1, 17), 16)

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return '\n'.join([str(i) for i in self.queue])

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        index = 0
        for i in range(len(self.queue)):
            if(self.queue[i][0] < self.queue[index][0]): #kolom 0 adalah cost maka akan dicari cost
                index = i
        item = self.queue[index]
        del self.queue[index]
        return item

class Node:
    def __init__(self,puzzle,prevMove,depth):
        self.puzzle = puzzle
        self.prevMove = prevMove
        self.depth = depth

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

# mencari nilai kurang(i) dari satu elemen
def totalKurang(list,a,i,j):
    sum = 0
    for b in range((i*4+j),len(list)):
        if(a > list[b] and list[b] != 0):
            sum += 1
        else:
            sum += 0
    return sum

# mencari posisi ubin kosong pada puzzle
def posisiKosong(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                if((i+j) % 2 == 0):
                    return 0,i,j
                else:
                    return 1,i,j

# nilai formula kurang(i) + posisi ubin kosong
def kurangi(puzzle,array): 
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += totalKurang(array,puzzle[i][j],i,j)
    posisikosong,_,_ = posisiKosong(puzzle)
    return (sum + posisikosong)

# mencari nilai cost dari bentuk puzzle terkini
def cost(puzzle,depth = 0):
    count = 0
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] != 16 and puzzle[i][j] != i*4+j+1):
                count += 1
    return (count+depth)

def move(puzzle,moveTo):
    temp = puzzle
    _,x,y = posisiKosong(puzzle)
    if(moveTo == "up" and x != 0):
        x-=1
    elif(moveTo == "down" and x != 3):
        x+=1
    elif(moveTo == "left" and y != 0):
        y-=1
    elif(moveTo == "right" and y != 3):
        y+=1

def swap(puzzle,i,j):
    _,x,y = posisiKosong(puzzle)
    temp = puzzle[i][j]
    puzzle[i][j] = puzzle[x][y]
    puzzle[x][y] = temp
    return puzzle

def lawanMove(prevMove):
    if(prevMove == "up"):
        return "down"
    elif(prevMove == "down"):
        return "up"
    elif(prevMove == "left"):
        return "right"
    elif(prevMove == "right"):
        return "left"

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