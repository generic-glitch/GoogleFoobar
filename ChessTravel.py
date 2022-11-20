# Solution here
def solution(src, dest):
  t = 0
  cNum = src
  if isCornerToCorner(src, dest):
    return 5
  else:
    while cNum != dest:
      l = getPossibleLocations(getRow(cNum), getCol(cNum))
      s = getClosestSolution(src, dest, l)
      cNum = getNum(s[0], s[1])
      t += 1
    return t

def isCornerToCorner(src, dest):
  if (getCol(src) == getCol(dest)) and (abs(src-dest) == 56):
    return True
  elif (getRow(src) == getRow(dest)) and (abs(src-dest) == 7):
    return True
  else:
    return False

def getPossibleLocations(row, column):
  possibleCombinations = [[row - 2, column - 1], [row + 2, column + 1],
                          [row + 2, column - 1], [row - 2, column + 1],
                          [row - 1, column - 2], [row + 1, column + 2],
                          [row - 1, column + 2], [row + 1, column - 2]]
  realCombinations = []
  for combination in possibleCombinations:
    if (combination[0] >= 0 and
        combination[0] <= 7) and (combination[1] >= 0 and combination[1] <= 7):
      realCombinations.append(combination)
  return realCombinations

def getClosestSolution(oNum, dest, sol):
  dRow = getRow(dest)
  dCol = getCol(dest)
  cSol = sol[0]
  cTot = abs(dRow - cSol[0]) + abs(dCol-cSol[1])
  for s in sol:
    if getNum(s[0], s[1]) == dest:
      return s
  for s in sol:
    sCol = s[1]
    sRow = s[0]
    if (abs(dRow-sRow) == 2) and (abs(dCol-sCol) == 1):
      return s
    elif (abs(dRow-sRow) == 1) and (abs(dCol-sCol) == 2):
      return s
  for s in sol:
    sCol = s[1]
    sRow = s[0]
    if getNum(s[0], s[1]) == oNum:
      continue
    else:
      if sRow == dRow and (abs(dCol - sCol) <= 2):
        return s
      elif dCol == sCol and (abs(dRow - sRow) <= 2):
        return s
  for s in sol:
    sCol = s[1]
    sRow = s[0]
    if getNum(s[0], s[1]) != oNum:
      if (abs(dRow - sRow) + abs(dCol - sCol)) <= cTot:
        cSol = s
        cTot = (abs(dRow - sRow) + abs(dCol - sCol))
  return cSol

def getNum(row, column):
  return ((row + 1) * (8)) - (8 - column)

def getRow(num):
  num2 = num
  amount = 0
  while num2 > 7:
    num2 -= 8
    amount += 1
  return amount

def getCol(num):
  return num % 8

print(solution(9, 0))