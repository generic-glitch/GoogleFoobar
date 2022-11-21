cache = {}
def solution(n):
  i = n
  p = 0
  for i in range(n-1, 1, -1):
    p += possibleAdditions(i, n, i)
  return p

def possibleAdditions(num, n, currentTotal=0):
  cacheStr = str(num)+str(n)+str(currentTotal)
  if cacheStr not in cache:
    p = 0
    for i in range(num-1, 0, -1):
      if (currentTotal + i) < n:
        p += possibleAdditions(i, n, currentTotal+i)
      elif (currentTotal+i) == n:
        p += 1
    cache[cacheStr] = p
    return p
  else:
    return cache[cacheStr]

print(solution(200))