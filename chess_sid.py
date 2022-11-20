board = [
  [0,   1, 2,  3,  4,   5,  6,  7], 
  [8,   9, 10, 11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20, 21, 22, 23], 
  [24, 25, 26, 27, 28, 29, 30, 31],
  [32, 33, 34, 35, 36, 37, 38, 39], 
  [40, 41, 42, 43, 44, 45, 46, 47],
  [48, 49, 50, 51, 52, 53, 54, 55], 
  [56, 57, 58, 59, 60, 61, 62, 63]]


def solution(src, dest):
  tries = 0
  c_num = src
  while c_num != dest:
    if reachable(c_num, dest):
      c_num = dest
      tries += 1
    elif is_next_to(dest, c_num):
      tries += is_next_to(dest, c_num)
      c_num = dest
    else:
      c_num = closest_num(possible_att(c_num), dest)
      tries += 1

  print(tries)


#distance between number and current num
def d_num(c_num, dest):
  return abs(c_num - dest)


def get_row(num):
  return num % 8


def requirements(n, num):
  if abs(get_row(n) - get_row(num)) <= 3 and n >= 0 and n <= 63:
    return n
  return None


def closest_num(lst, dest):
  clos_num = min(lst, key=lambda lst: abs(lst - dest))
  return clos_num


def possible_att(n):
  lst1 = [n + 6, n - 6, n + 17, n - 17, n - 10, n + 10, n + 15, n - 15]
  lst2 = []
  for loc in lst1:
    if requirements(loc, n):
      lst2.append(requirements(loc, n))

  return lst2


def reachable(c_num, dest):
  pos_loc_d = possible_att(dest)
  check = any(c_num in pos_loc_d for loc in pos_loc_d)
  return check


def is_next_to(dest, c_num):
  distance = d_num(c_num, dest)
  if distance == 7 or distance == 9:
    return 2
  if distance == 8 or distance == 1:
    return 3
  return None


solution(63,4)