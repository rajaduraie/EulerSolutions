def get_number_of_divisors(x):
  if (x == 1):
    return 1
  num_of_divisors = 2
  max = int(x/2)
  for i in range(2, max-1):
    if (x % i == 0):
      num_of_divisors = num_of_divisors + 2
      max = int(x/i)
    if (max < i*2):
      return num_of_divisors
  return num_of_divisors

found = 0
start = 1
num_to_find = start
while (found == 0):
  y = get_number_of_divisors(num_to_find)
  if (y > 500):
    print (num_to_find)
    found = 1
  start = start + 1
  num_to_find = num_to_find + start
