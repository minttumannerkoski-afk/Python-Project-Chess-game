class Square:
  def __init__(self, column, line, piece):
      self.column = column
      self.line = line
      self.piece = piece
     
board = [[Square(col, row) for row in range(1, 9)] for col in range(1, 9)]    

a1 = Square(1,1,0)
a2 = Square(1,2,0)
a3 = Square(1,3,0)
a4 = Square(1,4,0)
a5 = Square(1,5,0)
a6 = Square(1,6,0)
a7 = Square(1,7,0)
a8 = Square(1,8,0)

b1 = Square(2,1,0)
b2 = Square(2,2,0)
b3 = Square(2,3,0)
b4 = Square(2,4,0)
b5 = Square(2,5,0)
b6 = Square(2,6,0)
b7 = Square(2,7,0)
b8 = Square(2,8,0)

c1 = Square(3,1,0)
c2 = Square(3,2,0)
c3 = Square(3,3,0)
c4 = Square(3,4,0)
c5 = Square(3,5,0)
c6 = Square(3,6,0)
c7 = Square(3,7,0)
c8 = Square(3,8,0)

d1 = Square(4,1,0)
d2 = Square(4,2,0)
d3 = Square(4,3,0)
d4 = Square(4,4,0)
d5 = Square(4,5,0)
d6 = Square(4,6,0)
d7 = Square(4,7,0)
d8 = Square(4,8,0)

e1 = Square(5,1,0)
e2 = Square(5,2,0)
e3 = Square(5,3,0)
e4 = Square(5,4,0)
e5 = Square(5,5,0)
e6 = Square(5,6,0)
e7 = Square(5,7,0)
e8 = Square(5,8,0)

f1 = Square(6,1,0)
f2 = Square(6,2,0)
f3 = Square(6,3,0)
f4 = Square(6,4,0)
f5 = Square(6,5,0)
f6 = Square(6,6,0)
f7 = Square(6,7,0)
f8 = Square(6,8,0)

g1 = Square(7,1,0)
g2 = Square(7,2,0)
g3 = Square(7,3,0)
g4 = Square(7,4,0)
g5 = Square(7,5,0)
g6 = Square(7,6,0)
g7 = Square(7,7,0)
g8 = Square(7,8,0)

h1 = Square(8,1,0)
h2 = Square(8,2,0)
h3 = Square(8,3,0)
h4 = Square(8,4,0)
h5 = Square(8,5,0)
h6 = Square(8,6,0)
h7 = Square(8,7,0)
h8 = Square(8,8,0)