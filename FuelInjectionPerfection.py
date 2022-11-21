def solution(n):
  t = 0
  n = int(n)
  while n != 1:
    if n == 0:
      n += 1
    elif n % 2 == 0:
      n/=2
    elif n > -2 and n < 1:
      n += 1
    else:
      if possibleHalfs(n+1) > possibleHalfs(n-1) and n != 3:
        n+=1
      else:
        n-=1
    t += 1
  return t

def possibleHalfs(num):
  divisions = 0
  while num % 2 == 0:
    num/=2
    divisions += 1
  return divisions

print(solution(15))
print(solution(4))