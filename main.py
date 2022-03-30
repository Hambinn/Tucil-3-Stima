from ctypes import util
import utility
print("Masukkan nama file: ")
array =  utility.readfile(input())
puzzle = utility.listToMatrix(array)
utility.printPuzzle(puzzle)

if(utility.kurangi(puzzle,array) % 2 == 0):
    print("Solvable\n")
else:
    print("Unsolvable\n")

branch = []

while(utility.countG(puzzles) != 0):
    cost = 0
    utility.generateBranch(puzzle,branch)
    for i in range(len(branch)):







