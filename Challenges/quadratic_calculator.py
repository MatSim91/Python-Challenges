# Receives the user input for the quadratic equation
# numbers and calculates both roots.

from math import sqrt

def quadratic_equation():
  a = float(input("Insert the value for A: "))
  if a == 0:
    print("Not a quadratic equation. 'a' should not be zero.")
      
  else:
    b = float(input("Insert the value for B: "))
    
    c = float(input("Insert the value for C: "))

    delta = ((b) ** 2) - (4 * (a) * (c))
    if delta < 0:
      print("Complex roots!")
    else:
      delta_sqrt = sqrt(delta)
      
      print(delta_sqrt)
        
      x1 = (-(b) + delta_sqrt) / (2 * a)
      
      x2 = (-(b) - delta_sqrt) / (2 * a)
      
      print(f"x1 is: {x1}")
      
      print(f"x2 is: {x2}")

quadratic_equation()