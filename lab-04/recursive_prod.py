# a = number you're using
# b = how many times you adding a to itself # 

def rec_product(a, b):

  '''Calculate product a * b recursively'''
  
  if b == 0 : # base case 1 
    return 0
  elif b < 0  : # anything less than 0
    return -rec_product(a, -b)
  elif b == 1 : # base case 2
    return a
  else :
    return a + rec_product(a, b - 1)

print(rec_product(0, 5))
print(rec_product(1, 5))
print(rec_product(-1, 5))
print(rec_product(5, -1))
print(rec_product(-5, -1))