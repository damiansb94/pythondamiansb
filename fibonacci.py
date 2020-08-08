number1 = 1
number2 = 2
solution = 0
res = 0

while solution < 4000000:
 
 
 solution = number1 + number2
 number1 = number2
 number2 = solution
 if solution % 2 == 0:
  res = res + solution

print (solution, res+2)



 
