import copy

def minor(m, el):
    copy_matrix = copy.deepcopy(m)
    del copy_matrix[0]
    for i in range(len(copy_matrix[0]) - 1):
        del copy_matrix[i][el]
    return copy_matrix

def determinant(m):
    size = len(m)
    if size == 1:
        return m[0][0]
    det = 0
    sign = 1
    for j in range(size):
        det += m[0][j] * sign * determinant(minor(m, j))
        sign = sign * (-1)
    return det


a = determinant([[1,2,3],[2,5,6],[7,8,9]])
print(a)
