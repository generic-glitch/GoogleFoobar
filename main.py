def solution(l):
  l.sort(reverse=True)
  lList = largestList(l)
  lList.sort(reverse=True)
  if len(lList) < 1:
    return 0
  for i in range(len(lList)):
    sNum = lList[i]
    nNums = lList
    nNums.remove(sNum)
    totalNum = sNum
    for j in range(len(nNums)):
      num = nNums[j]
      totalNum = int(str(totalNum) + str(num))
    if totalNum % 3 == 0:
      return totalNum
  return 0

def largestList(l):
  newList = l
  newList.sort()
  for n in range(len(newList)):
    total = 0
    if n % 3 == 0:
      continue
    else:
      for num in newList:
        total += num
      if total % 3 != 0:
        removableNumbers(total, newList, n=0)
      if total % 3 == 0:
        return newList
  return []

def removableNumbers(total, list, n=0):
  nList = list
  nList.sort()
  if nList[n] % 3 == 0:
    if len(nList) > n+1:
      removableNumbers(total, nList, n+1)
  elif (total - nList[n]) % 3 == 0:
    nList.remove(nList[n])
    return
  else:`
    for i in range(len(nList)):
      if (total - nList[i]) % 3 == 0:
        nList.remove(nList[i])
        return
    if len(nList) > n:
      total -= nList[n]
      nList.remove(nList[n])
      removableNumbers(total, nList, n)
    
print(solution([9, 9, 4, 4, 3, 3, 1]))