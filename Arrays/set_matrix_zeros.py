def setZeroes(matrix):
    m, n = len(matrix[0]), len(matrix)
    col0 =1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if(j!=0):
                    matrix[0][j]=0
                else:
                    col0 =0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    if col0 == 0:
        for i in range(n):
            matrix[i][0]=0
    return matrix

if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("The Initial matrix is:")
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()
    setZeroes(matrix)
    print("The Final matrix is:")
    for row in matrix:
        for ele in row:
            print(ele, end=" ")
        print()  