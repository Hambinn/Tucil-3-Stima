import utility

print("pilih jenis input puzzle:")
print("1. input dari file")
print("2. input random")
pilihan = int(input("pilih: "))

if pilihan == 1:
    print("Masukkan nama file: ")
    array = utility.readfile(input())
    puzzle = utility.listToMatrix(array)
    print("Posisi Awal:")
    utility.printPuzzle(puzzle)
    utility.branchBound(puzzle, array)
else:
    array, puzzle = utility.generatePuzzle()
    utility.print_matrix(puzzle)
    utility.branchBound(puzzle, array)
