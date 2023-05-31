# The goal of this program is to practice Python constructs

def sumTwo(a,b):

   c = a + b

   return c

# modify this function to repeat

def getNumber():
  
  finalnumber = ""
  
  symbols = input("Enter a digit: ")
  
  number = int(symbols)
  
  while number != -1:
    finalnumber = finalnumber + str(number) 
    
    symbols = input("Enter a digit: ")
    
    number = int(symbols)
  
  return finalnumber

def sumDigits(x):

   # You will need to complete this function
   sum = 0

   while x != 0 :
     sum = sum + x % 10
     x = x // 10

   return sum

#added the race parameter to make wage calculation more specific
def convertWageMtoW(mWage, race):

   if race == "white":
     wageGap = 0.182
   elif race == "black":
     wageGap = 0.099
   elif race == "hispanic":
     wageGap = 0.13
   elif race == "asian":
     wageGap = 0.332

   ratio = 1 - wageGap

   return mWage * ratio

# test cases (given from assignment)   
print(convertWageMtoW(100, "white"))
print(convertWageMtoW(76.2, "asian"))
print(convertWageMtoW(0, "white"))

# own test cases
print(convertWageMtoW(34, "black"))
print(convertWageMtoW(94, "hispanic"))


userNumber = getNumber()
print(userNumber)
print("summed up: ", sumDigits(502))

x = sumTwo(3,5)

print(x)
