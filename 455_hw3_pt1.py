# Alida Hartwell
# CMSC 455
# HW3 Part 1A
# This program runs a trapezodial approximation of integrating sin(x) from 0 to 1

import math

def integrate(min, max, step):
  area = (math.sin(min) + math.sin(max)) / 2.0
  height = (max - min) / step
  
  for i in range(1, step + 1):
    xVal = min + (i*height)
    area += math.sin(xVal)
    
  return area * height

def getError(soln):
  actual = 1.0-math.cos(1.0)
  return (soln - actual)

def main():
  
  pointsList = [16, 32, 64, 128]
  
  for n in pointsList:
    val = integrate(0.0, 1.0, n)
    error = getError(val)
    print("For", n, "points, value is",val, "and error is", error)

main()
