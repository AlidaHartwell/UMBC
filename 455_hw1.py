# Homework 1
# Rocket Flight
# Alida Hartwell
# Uses given thrust values to calculate the maximum height of a rocket

def calcBodyFd(v):
  v2 = v * v
  return ((0.45 * 1.293 * 0.000506 * v2) / 2)

def calcFinsFd(v):
  v2 = v * v
  return ((0.01 * 1.293 * (0.00496) * v2) / 2)
  
def calcM(m, Ft):
  m = m - (0.001644 * Ft)
  if(m < 0.34 + 0.0094):
    return (0.034 + 0.0094)
  else:
    return m

def calcFg (m):
  return (m * 9.80665)
  
def calcF (v, m, ft):
  bodyFd = calcBodyFd(v)
  finsFd = calcFinsFd(v)
  Fg = calcFg(m)
  return (ft - (bodyFd + finsFd + Fg))

def calcA (F, m):
  return (F/m)

def calcDv (a, dt):
  return (a * dt)

def calcV (v, dv):
  return (v + dv)

def calcDs (v, dt):
  return (v * dt)

def calcS (s, ds):
  return (s + ds)

def main():
  t = 0 # time
  s = 0 # height
  v = 0 # velocity
  a = 0 # acceleration
  F = 0 # total force not including gravity
  m = 0.0340 + 0.0242 # mass
  dt = 0.1 # the change in time is always 0.1 second
  
  ftValues = [6, 12, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]  
  
  print("Values are printed in this order: time - height - velocity - acceleration - force - mass")
  while ((v > 0 or t == 0) and t < 6):
    
    t += dt
    t = round(t, 2)
    
    if (len(ftValues) > 0):
      ft = ftValues[0]
      ftValues = ftValues[1:]
    else:
      ft = 0
    
    m = calcM(m, ft)    
    F = calcF(v, m, ft)
    a = calcA(F, m)
    dv = calcDv(a, dt)
    v = calcV(v, dv)
    ds = calcDs(v, dt)
    s = calcS(s, ds)
  
    print(t, s, v, a, F, m)

main()
