from micrograd.node import Node
from micrograd.draw import draw_dot

n1 = Node(4.0)
print(n1)

n2 = Node(3.0)
print(n2)

draw_dot(n1)
draw_dot(n2)