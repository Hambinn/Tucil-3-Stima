import time
import utility


# Main Algorithm
print("Masukkan nama file: ")
array = utility.readfile(input())
puzzle = utility.listToMatrix(array)
utility.printPuzzle(puzzle)

if(utility.kurangi(puzzle, array) % 2 == 0):
    move = ("right", "down", "left", "up")
    print("Solvable\n")
    Queue = utility.PriorityQueue()
    generatedTree = 0

    simpul = utility.Node(puzzle)
    Queue.enqueue((utility.cost(simpul.matrix), simpul, "", 0))

    Queue_temp = Queue.dequeue()
    simpul = Queue_temp[1]
    New_Matrix = simpul.matrix
    Move_Balik = ""
    next_step = Queue_temp[3] + 1
    generatedTree += 1

    while(not utility.solved(New_Matrix)):
        for mov in move:
            if(mov != Move_Balik):
                after_move = utility.move(New_Matrix, mov)
                utility.printPuzzle(after_move)
                print()
                if(not utility.solved(after_move)):
                    new_simpul = utility.Node(after_move)
                    new_simpul.parent = simpul
                    new_simpul.depth = simpul.depth + 1
                    generatedTree += 1
                    Queue.enqueue(
                        (utility.cost(new_simpul.matrix, next_step), new_simpul, mov, next_step))

        Queue_temp = Queue.dequeue()
        simpul = Queue_temp[1]
        New_Matrix = simpul.matrix
        Move = Queue_temp[2]
        Move_balik = utility.lawanMove(Move)
        next_step = Queue_temp[3] + 1

    utility.printPuzzle(puzzle)

else:
    print("Unsolvable\n")
