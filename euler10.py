#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
import time
import math

def is_prime (x):
  if (x % 2 == 0):
    return 0
  if ( x == 3 ):
    return 1
  if (x < 9): 
    return 1

  f = 5
  sqrt_x = int(math.sqrt(x))
  while (f <= sqrt_x):
    if (x % f == 0):
      return 0
    if (x % (f+2) == 0):
      return 0
    f = f+6
  return 1

start_time = time.time()
plist = [2]

def sum_primes(min, max):
  if 2 >= min: yield 2
  for i in range(3, max, 2):
    if (is_prime(i)):
      plist.append(i)
      if i >= min: yield i
  return


val = sum(sum_primes(1, 2000000))
print val
print "%s is the time taken to finish execution "%(time.time() - start_time)

