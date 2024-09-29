
def printMatrix(A,starting_index,rows,columns):
    starting_row,starting_column = starting_index
    for i in range(starting_row,rows):
        for j in range(starting_column,columns):
            print(A[i][j] ,end=' ')
        print()

    


def MatAdd(A,B):
    if(len(A)!=len(B) or len(A[0])!=len(B[0])):
        return -1
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

def MatAddPartial(A,B,start,size):
    row_start,column_start = start
    num_rows,num_columns= size
    result = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            result[i][j] = A[i + row_start][j+column_start] + B[i+row_start][j+column_start]
    return result

def MatMul(A,B):
    if(len(A[0]) != len(B)):
        return -1
    # initialize the result matrix with 0s of size len(A[0]) x len(B)
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += (A[i][k] * B[k][j])
    return result


            
            

def printMatrix(A,starting_index,rows,columns):
    starting_row,starting_column = starting_index
    for i in range(starting_row,rows):
        for j in range(starting_column,columns):
            print(A[i][j] ,end=' ')
        print()

    


def MatAdd(A,B):
    if(len(A)!=len(B) or len(A[0])!=len(B[0])):
        return -1
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result

def MatAddPartial(A,B,start,size):
    row_start,column_start = start
    num_rows,num_columns= size
    result = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            result[i][j] = A[i + row_start][j+column_start] + B[i+row_start][j+column_start]
    return result

def MatMul(A,B):
    if(len(A[0]) != len(B)):
        return -1
    # initialize the result matrix with 0s of size len(A[0]) x len(B)
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j] += (A[i][k] * B[k][j])
    return result


            
            
def MatMulRecursive(A,B):
    if(len(A[0]) != len(B)):
        return -1
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    def Recursive(A,B,i,j,k):
        if(i==len(A)):
            return
        if(j==(len(B[0]))):
            Recursive(A,B,i+1,0,0)
            return
        if(k==len(B)):
            Recursive(A,B,i,j+1,0)
            return
        result[i][j] += A[i][k] *B[k][j]
        Recursive(A,B,i,j,k+1)

    Recursive(A,B,0,0,0)
    return result


# Example usage:
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result = MatMulRecursive(A, B)
for row in result:
    print(row)
    



    






    
