from display import *
from draw import *
from matrix import *
from math import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

m2 = new_matrix(0, 0)
add_edge(m2, 1, 2, 3, 4, 5, 6)
print("\nTesting add_edge. Adding (1,2,3) and (4,5,6) to m2.")
print_matrix(m2)

m1 = new_matrix()
ident(m1)
print("\nTesting ident on m1")
print_matrix(m1)

matrix_mult(m1, m2)
print("\nTesting matrix_mult on m1 * m2")
print_matrix(m2)

m1 = new_matrix(0,0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print("\nTesting adding new edges to m1")
print_matrix(m1)

matrix_mult(m1, m2)
print("\nTesting matrix_mult again on m1 * m2")
print_matrix(m2)

print("\nTesting draw_lines on m1")
draw_lines( m1, screen, color )
print("\nTesting draw_lines on m2")
draw_lines( m2, screen, color )

display(screen)
