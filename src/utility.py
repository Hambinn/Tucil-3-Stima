import random
import time
target = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
moveset = ("right", "down", "left", "up")


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
            if(self.queue[i][0] < self.queue[index][0]):
                index = i
        item = self.queue[index]
        del self.queue[index]
        return item


class Node:
    def __init__(self, data=None):
        self.matrix = data
        self.parent = None
        self.depth = 0


def generatePuzzle():
    listRandom = random.sample(range(1, 17), 16)
    puzzle = listToMatrix(listRandom)
    return listRandom, puzzle


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
def totalKurang(list, a, i, j):
    sum = 0
    for b in range((i*4+j), len(list)):
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
                    return 0, i, j
                else:
                    return 1, i, j

# nilai formula kurang(i) + posisi ubin kosong
def kurangi(puzzle, array):
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += totalKurang(array, puzzle[i][j], i, j)
    posisikosong, _, _ = posisiKosong(puzzle)
    return (sum + posisikosong)

# mencari nilai cost dari bentuk puzzle terkini
def cost(depth, matrix):
    sum = 0
    for i in range(4):
        for j in range(4):
            if((matrix[i][j] != target[i][j]) and matrix[i][j] !=16):
                sum += 1
    return (depth+sum)


def moveTiles(puzzle, movement):
    matrixCopy = copyMatrix(puzzle)
    _, x, y = posisiKosong(matrixCopy)
    if(movement == "left" and y != 0):
            y -= 1
    elif(movement == "right" and y != 3):
            y += 1
    elif(movement == "up" and x != 0):
            x -= 1
    elif(movement == "down" and x != 3):
            x += 1
    matrixCopy = swap(matrixCopy, x, y)
    return matrixCopy


def swap(matrix, row, column):
    _, x, y = posisiKosong(matrix)
    matrix[x][y] = matrix[row][column]
    matrix[row][column] = 16
    return matrix


def lawanMove(prevMove):
    if(prevMove == "up"):
        return "down"
    elif(prevMove == "down"):
        return "up"
    elif(prevMove == "left"):
        return "right"
    elif(prevMove == "right"):
        return "left"

def solved(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != target[i][j]):
                return False
    return True


def printPuzzle(matrix):
    print("╔═══╦═══╦═══╦═══╗")
    for i in range(4):
        for j in range(4):
            print("║ ", end="")
            if(matrix[i][j] == 16):
                print("  ", end="")
            else:
                print(matrix[i][j], end="")
            if(matrix[i][j] < 10):
                print(" ", end="")
        print("║")
        if(i != 3):
            print("╠═══╬═══╬═══╬═══╣")
    print("╚═══╩═══╩═══╩═══╝")


def solved(matrix, target):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != target[i][j]):
                return False
    return True


def copyMatrix(matrix):
    newMatrix = [[0 for a in range(4)] for b in range(4)]
    for i in range(4):
        for j in range(4):
            newMatrix[i][j] = matrix[i][j]
    return newMatrix


def printStep(node):
    if(node.parent == None):
        return
    printStep(node.parent)
    print("\n")
    print("Langkah "+str(node.depth)+" : ")
    printPuzzle(node.matrix)

def printKurangi(puzzle, array):
    for i in range(4):
        for j in range(4):
            print("Fungsi kurang (" ,puzzle[i][j], ") = ", totalKurang(array, puzzle[i][j], i, j))
    print("Total Fungsi Kurangi  + posisi ubin = ", kurangi(puzzle, array))


def branchBound(puzzle, array):
    if(kurangi(puzzle, array) % 2 == 0):
        timeStart = time.time()
        printKurangi(puzzle, array)
        print("Solvable Puzzle\n")
        Queue = PriorityQueue()
        generatedNode = 0

        simpul = Node(puzzle)
        Queue.enqueue((cost(0, simpul.matrix), simpul, "", 0))

        tempQueue = Queue.dequeue()
        simpul = tempQueue[1]
        matrixMove = simpul.matrix
        prevMove = ""
        depth = tempQueue[3] + 1
        generatedNode += 1

        while(not solved(matrixMove, target)):
            for mov in moveset:
                if(mov != prevMove):
                    after_move = moveTiles(matrixMove, mov)
                    if(not solved(after_move, matrixMove)):
                        newNode = Node(after_move)
                        newNode.parent = simpul
                        newNode.depth = simpul.depth + 1
                        generatedNode += 1
                        Queue.enqueue(
                            (cost(depth, newNode.matrix), newNode, mov, depth))

            tempQueue = Queue.dequeue()
            simpul = tempQueue[1]
            matrixMove = simpul.matrix
            moveNew = tempQueue[2]
            prevMove = lawanMove(moveNew)
            depth = tempQueue[3] + 1
        timeEnd = time.time()
        timeEstimated = timeEnd - timeStart
        printStep(simpul)
        print("Waktu yang diperlukan = ", timeEstimated, "detik")
        print("Jumlah simpul yang dihasilkan = ", generatedNode)

    else:
        printKurangi(puzzle, array)
        print("Unsolvable Puzzle\n")
