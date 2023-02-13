print("You can perform various operations on matrix\n"
      "1.Determinant\n"
      "2.Adjoint\n"
      "3.Cramer Rule\n"
      "4.Inverse")
choice = int(input("Enter the number of the operation which you want to perform for example, if you "
                   "want to find determinant enter 1 and for inverse enter 4 and so on:"))
if choice == 1:
    # Process
    # First convert the matrix to row echelon form and then mutilply the diagonal elements
    def inputMatrix():
        rows = int(input("Enter number of rows of matrix:"))
        cols = int(input("Enter number of columns of matrix:"))
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                number = float(input(f"Enter the number for row {i + 1} and column {j + 1}:"))
                row.append(number)
            matrix.append(row)
        return matrix


    def findDeterminant():
        matrix = inputMatrix()
        ans = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == col:
                    pe = matrix[row][col]
                    ans.append(pe)  # Stores the diagonal elements
                    if pe != 0:
                        for r in range(len(matrix[0])):
                            matrix[row][r] = round(matrix[row][r] / pe, 3)
                        for j in range(len(matrix)):
                            if j > row:
                                makeZero = matrix[j][col]
                                for k in range(len(matrix[0])):
                                    matrix[j][k] = round(matrix[j][k] - matrix[row][k] * makeZero, 3)
        result = 1
        for r in range(len(ans)):
            result *= ans[r]
        return round(result)


    print(findDeterminant())
elif choice == 2:
    def inputMatrix():
        rows = int(input("Enter number of rows of matrix:"))
        cols = int(input("Enter number of columns of matrix:"))
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                number = float(input(f"Enter the number for row {i + 1} and column {j + 1}:"))
                row.append(number)
            matrix.append(row)
        return matrix


    def findMinor(mat, x, y):
        ans = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row == col:  # make sure to only make 1 only the diagonal elements
                    pe = mat[row][col]
                    ans.append(pe)  # Stores the diagonal elements
                    if pe != 0:
                        for r in range(len(mat[0])):
                            mat[row][r] = round(mat[row][r] / pe, 3)
                        for j in range(len(mat)):
                            if j > row:
                                makeZero = mat[j][col]
                                for k in range(len(mat[0])):
                                    mat[j][k] = round(mat[j][k] - mat[row][k] * makeZero, 3)
        result = 1
        # This part mutliplies the diagonal numbers
        for r in range(len(ans)):
            result *= ans[r]
        res = round(result)
        # This part checks for the sign of the cofactor
        signOfCofactor = x + y
        if signOfCofactor % 2 == 0:
            return res
        else:
            res *= -1
            return res


    def printMatrix(adjMatrix):
        print("The adjoint of the given matrix is:")
        for i in adjMatrix:
            for j in i:
                print("%10.3F" % j, end=" ")
            print()


    def transposeMatrix(coMatrix, oMatrix):
        adjointMatrix = []
        for i in range(len(coMatrix)):
            rows = []
            for j in range(len(oMatrix[0])):
                num = coMatrix[j][i]
                rows.append(num)
            adjointMatrix.append(rows)
        return adjointMatrix


    def findAdjoint():
        # This will take matrix as input
        m = inputMatrix()
        '''This code first go through each element of matrix,and delete it's row and column and finds the
        determinant of the new obtained matrix.And,if the row + column is even,then don't change the sign of determinant 
        otherwise,change the sign of determinant '''
        cofactorMatrix = []  # It stores the minors of every position i,j
        for i in range(len(m)):
            r = []
            for j in range(len(m[0])):
                newMinorMatrix = []  # It returns a new minor matrix for each number
                for k in range(len(m)):
                    row = []
                    for l in range(len(m[0])):
                        if k == i:  # It is for the deletion of row
                            continue
                        elif l == j:  # It is for the deletion of column
                            continue
                        else:
                            row.append(m[k][l])
                    if row != []:
                        newMinorMatrix.append(row)
                # It returns the cofactor of every position i,j
                Cofactor = findMinor(newMinorMatrix, i, j)
                r.append(Cofactor)
            cofactorMatrix.append(r)
        # It will return the transpose of cofactor matrix
        adjointMatrix = transposeMatrix(cofactorMatrix, m)
        # It will print the result to the screen
        printMatrix(adjointMatrix)


    findAdjoint()
elif choice == 3:
    '''In this method,We take two inputs,a matrix of coefficients of variables
    and a matrix of right hand side coefficients.
    Calculate a determinant of the main (square) matrix.
    To find the 'i'th solution of the system of linear equations using
    Cramer's rule replace the 'i'th column of the main matrix by solution
    vector and calculate its determinant. Then divide this determinant by
    the main one - this is one part of the solution set, determined using
    Cramer's rule. Repeat this operation for each variable.
    For determinant calculation,we use gaussian elimination method.'''
    import copy


    def findDeterminant(m):
        ans = []
        for row in range(len(m)):
            for col in range(len(m[0])):
                if row == col:
                    pe = m[row][col]
                    ans.append(pe)  # Stores the diagonal elements
                    if pe != 0:
                        for r in range(len(m[0])):
                            m[row][r] = round(m[row][r] / pe, 3)
                        for j in range(len(m)):
                            if j > row:
                                makeZero = m[j][col]
                                for k in range(len(m[0])):
                                    m[j][k] = round(m[j][k] - m[row][k] * makeZero, 3)
        result = 1
        for r in range(len(ans)):
            result *= ans[r]
        return round(result)


    def cramerRule():
        matrixDimension = int(input('Enter the dimension of matrix:'))
        variables = []
        for i in range(matrixDimension):
            variable = input("Enter the variables of the equation one by one:")
            variables.append(variable)
        matrix = []  # This is the matrix of coefficients on the left hand side
        for i in range(matrixDimension):
            row = []
            for j in range(matrixDimension):
                number = float(input(f"Enter the number for row {i + 1} and column {j + 1}:"))
                row.append(number)
            matrix.append(row)
        # This is the matrix of coefficients of right hand side
        constants = []
        for i in range(matrixDimension):
            number = int(input('Enter the right hand side coefficients one by one:'))
            constants.append(number)
        # Making a copy of main matrix because the original matrix
        # will get change after finding its determinant
        copyMatrix = copy.deepcopy(matrix)
        # Here,we are calculating the determinant of main matrix
        det = findDeterminant(matrix)
        # It the matrix is singular
        if det == 0:
            print("The solution of this system doesn't exist.")
        else:  # If the matrix is non-singular
            for i in range(matrixDimension):
                newMatrix = []  # This is the new matrix after changing the column with right hand side coefficients
                for j in range(len(copyMatrix)):
                    row = []
                    for k in range(len(copyMatrix[0])):
                        if k == i:
                            row.append(constants[j])
                        else:
                            row.append(copyMatrix[j][k])
                    newMatrix.append(row)
                # determinant of new matrix
                detOfNewMatrix = round(findDeterminant(newMatrix), 3)
                ans = detOfNewMatrix / det
                print(f"{variables[i]} = {ans}")


    cramerRule()
else:
    import copy


    def inputMatrix():
        rows = int(input("Enter number of rows of matrix:"))
        cols = int(input("Enter number of columns of matrix:"))
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                number = float(input(f"Enter the number for row {i + 1} and column {j + 1}:"))
                row.append(number)
            matrix.append(row)
        return matrix


    def findDeterminant(matrix):
        """In this method,we first reduce the matrix to row echelon form and then,multilpy the
        diagonal elements"""
        ans = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == col:
                    pe = matrix[row][col]
                    ans.append(pe)  # Stores the diagonal elements
                    if pe != 0:
                        for r in range(len(matrix[0])):
                            matrix[row][r] = round(matrix[row][r] / pe, 3)
                        for j in range(len(matrix)):
                            if j > row:
                                makeZero = matrix[j][col]
                                for k in range(len(matrix[0])):
                                    matrix[j][k] = round(matrix[j][k] - matrix[row][k] * makeZero, 3)
        result = 1
        for r in range(len(ans)):
            result *= ans[r]  # Multiplying all the diagonal elements to get the determinant
        return round(result)


    def findMinor(mat, x, y):
        """In this part,we are calculating the determinant"""
        res = findDeterminant(mat)
        # This part checks for the sign of the cofactor
        signOfCofactor = x + y
        if signOfCofactor % 2 == 0:  # If the position of number is even,then,don't change the sign
            return res
        else:  # Otherwise,change the sign of the cofactor
            res *= -1
            return res


    def printMatrix(adjMatrix):
        for i in adjMatrix:
            for j in i:
                print("%10.3F" % j, end=" ")
            print()


    def findTranspose(coMatrix, oMatrix):
        adjointMatrix = []
        for i in range(len(coMatrix)):
            rows = []
            for j in range(len(oMatrix[0])):
                num = coMatrix[j][i]
                rows.append(num)
            adjointMatrix.append(rows)
        return adjointMatrix


    def findAdjoint(m):
        cofactorMatrix = []  # It stores the minors of every position i,j
        for i in range(len(m)):
            r = []
            for j in range(len(m[0])):
                newMinorMatrix = []  # It returns a new minor matrix for each number
                for k in range(len(m)):
                    row = []
                    for l in range(len(m[0])):
                        if k == i:  # It is for the deletion of row
                            continue
                        elif l == j:  # It is for the deletion of column
                            continue
                        else:
                            row.append(m[k][l])
                    if row != []:
                        newMinorMatrix.append(row)
                # It returns the cofactor of every position i,j
                Cofactor = findMinor(newMinorMatrix, i, j)
                r.append(Cofactor)
            cofactorMatrix.append(r)
        # It will return the transpose of cofactor matrix
        adjointMatrix = findTranspose(cofactorMatrix, m)
        return adjointMatrix


    def findInverse():
        matrix = inputMatrix()
        # Making a deepcopy because the matrix will get change after determinant operation and in most of the
        # places we will need original matrix
        copyMatrix = copy.deepcopy(matrix)
        determinant = findDeterminant(matrix)
        if determinant != 0:
            print("It's a non-singular matrix.The inverse is:")
            adjMatrix = findAdjoint(copyMatrix)
            # inverse = adjoint / determinant
            # This code divides the each element of adjoint matrix by determinantcopy.deep
            inverseMatrix = []
            for i in range(len(adjMatrix)):
                row = []
                for j in range(len(adjMatrix[0])):
                    entry = adjMatrix[i][j] / determinant
                    row.append(entry)
                inverseMatrix.append(row)
            # This will print the result
            printMatrix(inverseMatrix)
        else:
            print("It's a singular matrix.So the inverse can't be calculated.")


    findInverse()

