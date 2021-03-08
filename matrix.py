"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    #print(matrix)
    for i in range(len(matrix[0])):
        row = ""
        for arr in matrix:
            row+=(str(arr[i])+"\t")
        print(row)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for c in range(len(matrix)):
        for r in range(len(matrix[c])):
            if (r == c):
                matrix[c][r] = 1.0
            else:
                matrix[c][r] = 0.0


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    tmp = []
    for arr in m2:
        tmp.append(arr[:])

    for i in range(len(m1[0])):
        for j in range(len(tmp)):
            f = []
            for k in range(len(m1)):
                f.append(m1[k][i] * tmp[j][k])
            m2[j][i] = float(sum(f))


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
