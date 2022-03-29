import utility
print("Masukkan nama file: ")
array =  utility.readfile(input())
puzzle = utility.listToMatrix(array)
utility.printPuzzle(puzzle)

if(utility.kurangi(puzzle,array) % 2 == 0):
    print("Solvable")
else:
    print("Unsolvable")

utility.printPuzzle(utility.moveUp(puzzle))