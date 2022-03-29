import utility
print("Masukkan nama file: ")
array =  utility.readfile(input())
puzzle = utility.listToMatrix(array)
print(array)

if(utility.kurangi(puzzle,array) % 2 == 0):
    print(utility.kurangi(puzzle,array))
    print("Solvable")
else:
    print("Unsolvable")

print(utility.countG(puzzle))