def display_matrix(lst):
    for i in lst:
        for j in i:
            print(round(j, 2), end = "\t")
        print()

def multiply(n, a, b):
    mul = []

    for i in range(n):
        row = []
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * b[k][j]
            row.append(sum)
        mul.append(row)

    return mul

def identity(n):
    lst = list()

    for i in range(n):
        row = []
        for j in range(n):
            row.append(1 if i == j else 0)
        lst.append(row)    

    return lst

def permutation(n, row1, row2):
    lst = identity(n)

    lst[row1], lst[row2] = lst[row2], lst[row1]

    return lst

def row_swap(n, A, row1, row2):
    lst = permutation(n, row1, row2)

    return multiply(n, lst, A)

def col_swap(n, A, col1, col2):
    lst = permutation(n, col1, col2)

    return multiply(n, A, lst)

def max_pivot(n, ind, A, B):
    max = ind

    for i in range(ind+1, n):
        if abs(A[i][ind]) > abs(A[max][ind]):
            max = i

    if max != ind:
        lst = row_swap(n, A, ind, max)
        inv = row_swap(n, B, ind, max)
        return lst, inv

    return A, B

def row_reduction(n, A, B, col, row, fact):
    iden = identity(n)
    iden[col][row] = fact

    lst = multiply(n, iden, A)
    inv = multiply(n, iden, B)

    return lst, inv

def row_elimination(n, A, B, ind, fact):
    for i in range(n):
        A[ind][i] /= fact
        B[ind][i] /= fact

    return A, B

A = [
    [1, 2],
    [0, 1]
]

B = identity(len(A))

lst = [row[:] for row in A]
inv = [row[:] for row in B]

for i in range(len(A)):
    lst, inv = max_pivot(len(lst), i, lst, inv)
    pivot = lst[i][i]
    for j in range(i+1, len(lst)):
        ele = lst[j][i]
        if ele != 0:
            factor = -1 * (ele/pivot)
            lst, inv = row_reduction(len(lst), lst, inv, j, i, factor)

for i in range(len(A) - 1, -1, -1):
    pivot = lst[i][i]
    lst, inv = row_elimination(len(lst), lst, inv, i, pivot)
    for j in range(i-1, -1, -1):
        ele = lst[j][i]
        if ele != 0:
            factor = -1 * ele
            lst, inv = row_reduction(len(lst), lst, inv, j, i, factor)

print("\n========= INVERSE MATRIX CALCULATOR =========\n")
print("\n=========      ACTUAL MATRIX        =========\n")
display_matrix(A)
print("\n=========      INVERSE MATRIX       =========\n")
display_matrix(inv)