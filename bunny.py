#+1 intervals up and down
def answer(x, y):
  z = ((x+y-1)*(x+y-2))/2 + x #adds x to y then subtracts 1 from it--. Multiplies that by x plus y minus 2 to get a base. It then divides all of this by 2 and eventually adds x to the quotient.
  return str(z)
print(answer(5, 10))