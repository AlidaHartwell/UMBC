# Alida Hartwell
# CMSC 455
# HW3 Part 2
# Approximates the area inside of two circles and outside of a third

# Check if dot is inside circle 2, then inside circle 3, then NOT inside circle 1
import decimal

def drange(a, b, jump):
  while a < b:
    yield float(a)
    a += decimal.Decimal(jump)

# Tests if point (x,y) is in circle 1
# Returns true if point outside circle
def outside1(x, y):
  ans = ((x-2)**2) + ((y-2)**2)
  return ans > 1

# Returns true if point inside circle 2
def inside2(x,y):
  ans = (x**2) + ((y-2)**2)
  return ans <= 4

# Returns true if point inside circle 3
def inside3(x,y):
  ans = (x**2) + (y**2)
  return ans <= 9

# Return true if inside desired area
def inArea(x,y):
  o1 = outside1(x,y)
  i2 = inside2(x,y)
  i3 = inside3(x,y)
  return (o1 and i2 and i3)
  

# Checks for points in the ranges:
# X: [-2, 2]
# Y: [0,3]
def main():
  
  steps = [0.1, 0.01, 0.001]
  
  for step in steps:
    xPt = -2
    area = 0
    ptsInside = 0
    while xPt < (2+step):
      yPt = 0
      while yPt < (3+step):
        ans = inArea(xPt, yPt)
        if ans:
          ptsInside += 1
        yPt += step
      xPt += step
    area = (step**2) * ptsInside
    print("For step size", step, "area is", area)
  
main()
