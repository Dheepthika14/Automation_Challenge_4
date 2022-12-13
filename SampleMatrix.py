def MatrixList(rows, cols, a):
    strt_Row = 0
    strt_Col = 0

    while strt_Row < rows and strt_Col < cols:
        for i in range(strt_Col, cols):
            print(a[strt_Row][i], end=" ")

        strt_Row = strt_Row + 1

        for i in range(strt_Row, rows):
            print(a[i][cols - 1], end=" ")

        cols = cols - 1

        if strt_Row < rows:

            for i in range(cols - 1, (strt_Col - 1), -1):
                print(a[rows - 1][i], end=" ")

            rows = rows - 1

        if strt_Col < cols:
            for i in range(rows - 1, strt_Row - 1, -1):
                print(a[i][strt_Col], end=" ")

            strt_Col = strt_Col + 1


R = int(input("Enter the no of Rows: "))
C = int(input("Enter the no of Columns: "))
matrix = []
print("Enter each values in new line")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()

MatrixList(R, C, matrix)
