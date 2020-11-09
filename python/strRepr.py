class Point: #Python 実践入門 P.189
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __repr__(self):
    return f'Point({self.x}, {self.y})'
  def __str__(self):
    return f'({self.x}, {self.y})'

if __name__ == "__main__":
  p = Point(1, 2)
  p
  print(p)



