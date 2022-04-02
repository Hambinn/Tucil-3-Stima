from imp import new_module
import time
import utility

final = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Main Algorithm

print("pilih jenis input puzzle:")
print("1. input dari file")
print("2. input random")
pilihan = int(input("pilih: "))

if pilihan == 1:
    print("Masukkan nama file: ")
    array = utility.readfile(input())
    puzzle = utility.listToMatrix(array)
    utility.printPuzzle(puzzle)

    

else:
    array, puzzle = utility.generatePuzzle()

    utility.print_matrix(puzzle)

    if(utility.kurangi(puzzle, array) % 2 == 0):
        move = ("right", "down", "left", "up")
        print("Solvable\n")
        Queue = utility.PriorityQueue()
        generatedTree = 0

        simpul = utility.Node(puzzle)
        Queue.enqueue((utility.cost(0, simpul.matrix, final), simpul, "", 0))

        Queue_temp = Queue.dequeue()
        simpul = Queue_temp[1]
        New_Matrix = simpul.matrix
        utility.print_matrix(New_Matrix)
        Move_balik = ""
        next_step = Queue_temp[3] + 1
        generatedTree += 1

        while(not utility.equal(New_Matrix, final)):
            for mov in move:
                if(mov != Move_balik):
                    after_move = utility.move(New_Matrix, mov)
                    # utility.print_matrix(after_move)
                    # print()
                    # utility.print_matrix(New_Matrix)
                    if(not utility.equal(after_move, New_Matrix)):
                        print("masuk sini")
                        new_simpul = utility.Node(after_move)
                        new_simpul.parent = simpul
                        new_simpul.depth = simpul.depth + 1
                        generatedTree += 1
                        Queue.enqueue(
                            (utility.cost(next_step, new_simpul.matrix, final), new_simpul, mov, next_step))

            Queue_temp = Queue.dequeue()
            simpul = Queue_temp[1]
            New_Matrix = simpul.matrix
            Move = Queue_temp[2]
            Move_balik = utility.lawanMove(Move)
            next_step = Queue_temp[3] + 1

        utility.print_matrix(puzzle)
        utility.print_path(simpul)

    else:
        print("Unsolvable\n")
