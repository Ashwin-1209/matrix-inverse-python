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

def row_reduction(n, A, col, row, fact):
    iden = identity(n)
    iden[col][row] = fact

    lst = multiply(n, iden, A)

    return lst

A = [
    [1, 2],
    [2, 3]
]

lst = [row[:] for row in A]
for i in range(len(A)):
    pivot = lst[i][i]
    print("Pivot ", i+1, ":", pivot)
    for j in range(i+1, len(lst)):
        ele = lst[j][i]
        if ele != 0:
            factor = -1*(ele/pivot)
            lst = row_reduction(len(lst), lst, j, i, factor)

print(lst)