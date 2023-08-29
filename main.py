def isItATriangle(**allSides):

  # Fourth side is an additional side to the equation.
  
  checkOne = False
  checkTwo = False
  checkThree = False
  checkFour = False

  # 1, 2, and 3.
  
  if firstSide + secondSide > thirdSide:
    checkOne = True
  if secondSide + thirdSide > firstSide:
    checkTwo = True
  if thirdSide + firstSide > secondSide:
    checkThree = True
    
  # 1, 2, and 4. (They can't be the last in the line).
  # 2, 3, and 4.
  # 1, 3, and 4.
  
  if (fourthSide + firstSide > secondSide and fourthSide + secondSide > firstSide and firstSide + secondSide > fourthSide) or\
  (fourthSide + secondSide > thirdSide and fourthSide + thirdSide > secondSide and secondSide + thirdSide > fourthSide) or\
  (fourthSide + firstSide > thirdSide and fourthSide + thirdSide > firstSide and firstSide + thirdSide > fourthSide):
    checkFour = True

  answers = (checkOne, checkTwo, checkThree, checkFour)
  count = 0
  
  for i in answers:
    if i == True:
      count += 1

  if count >= 3:
    return True
  else:
    return False

###

firstSide = int(input("Digite o primeiro lado do triângulo: "))
secondSide = int(input("Digite o segundo lado do triângulo: "))
thirdSide = int(input("Digite o terceiro lado do triângulo: "))
fourthSide = int(input("Digite o quarto lado do triângulo: "))

if isItATriangle(firstSide = firstSide, secondSide = secondSide, thirdSide = secondSide, fourthSide = fourthSide):
  print("S")
else:
  print("N")