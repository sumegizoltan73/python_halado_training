
# list comprehensions 2. - lista megértések 2.

matrix_zeros = [[0 for x in range(4)] for y in range(4)]

# print(matrix_zeros)

matrix_print = lambda mat: ([print(row) for row in mat], print())

matrix_print(matrix_zeros)

matrix_identity = [[1 if x==y else 0 for x in range(4)] for y in range(4)]

matrix_print(matrix_identity)