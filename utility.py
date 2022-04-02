import random
ans = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]


def generatePuzzle():
    listRandom = random.sample(range(1, 17), 16)
    puzzle = listToMatrix(listRandom)
    return listRandom, puzzle


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
            # kolom 0 adalah cost maka akan dicari cost
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


def cost(depth, matrix, ans):
    counter = 0
    for i in range(4):
        for j in range(4):
            if((matrix[i][j] != ans[i][j]) and matrix[i][j] != 0):
                counter += 1
    return (depth+counter)


def move(puzzle, movement):
    matrix_temp = copyMatrix(puzzle)
    _, x, y = posisiKosong(matrix_temp)
    if(movement == "left"):
        if(y != 0):
            y -= 1
    elif(movement == "right"):
        if(y != 3):
            y += 1
    elif(movement == "up"):
        if(x != 0):
            x -= 1
    elif(movement == "down"):
        if(x != 3):
            x += 1
    matrix_temp = swap(matrix_temp, x, y)
    return matrix_temp


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


def printPuzzle(puzzle):
    for i in range(4):
        for j in range(4):
            if(puzzle[i][j] == 16):
                print("  ", end="")
            else:
                print(puzzle[i][j], end=" ")
        print()


def solved(matrix):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != ans[i][j]):
                return False
    return True


def print_matrix(matrix):
    print("╔═══╦═══╦═══╦═══╗")
    for i in range(4):
        for j in range(4):
            print("║ ", end="")
            print(matrix[i][j], end="")
            if(matrix[i][j] < 10):
                print(" ", end="")
        print("║")
        if(i != 3):
            print("╠═══╬═══╬═══╬═══╣")
    print("╚═══╩═══╩═══╩═══╝")


def equal(matrix, ans):
    for i in range(4):
        for j in range(4):
            if(matrix[i][j] != ans[i][j]):
                return False
    return True


def copyMatrix(matrix):
    newMatrix = [[0 for a in range(4)] for b in range(4)]
    for i in range(4):
        for j in range(4):
            newMatrix[i][j] = matrix[i][j]
    return newMatrix


def print_path(node):
    if(node.parent == None):
        return
    print_path(node.parent)
    print("\n======================")
    print("Move "+str(node.depth)+" : ")
    print_matrix(node.matrix)

def branchBound(puzzle,array):
    if(kurangi(puzzle, array) % 2 == 0):
        move = ("right", "down", "left", "up")
        print("Solvable\n")
        Queue = PriorityQueue()
        generatedTree = 0

        simpul = Node(puzzle)
        Queue.enqueue((cost(0, simpul.matrix, ans), simpul, "", 0))

        Queue_temp = Queue.dequeue()
        simpul = Queue_temp[1]
        New_Matrix = simpul.matrix
        print_matrix(New_Matrix)
        Move_balik = ""
        next_step = Queue_temp[3] + 1
        generatedTree += 1

        while(not equal(New_Matrix, final)):
            for mov in move:
                print(mov)
                if(mov != Move_balik):
                    after_move = move(New_Matrix, mov)
                    # utility.print_matrix(after_move)
                    # print()
                    # utility.print_matrix(New_Matrix)
                    if(not equal(after_move, New_Matrix)):
                        new_simpul = Node(after_move)
                        new_simpul.parent = simpul
                        new_simpul.depth = simpul.depth + 1
                        generatedTree += 1
                        Queue.enqueue(
                            (cost(next_step, new_simpul.matrix, final), new_simpul, mov, next_step))

            Queue_temp = Queue.dequeue()
            simpul = Queue_temp[1]
            New_Matrix = simpul.matrix
            Move = Queue_temp[2]
            Move_balik = lawanMove(Move)
            next_step = Queue_temp[3] + 1
            print_matrix(New_Matrix)

        utility.print_matrix(puzzle)
        utility.print_path(simpul)

    else:
        print("Unsolvable\n")