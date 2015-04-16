import sys
import time
import math

def is_prime (x):
  if (x % 2 == 0):
    return 0
  if (x % 3 == 0):
    return 0
  if (x < 9 ):
    return 1
  sqrt_x = int(math.sqrt(x))
  f = 5
  while ( f <= sqrt_x):
    if (x % f == 0):
      return 0
    if ( x % (f+2) == 0):
      return 0
    f = f + 6
  return 1

start_time = time.time()
primes = []
primes.append(2)
primes.append(3)

prime = 5
i = 3
j=7
while (i<=10000):
  if(is_prime(j)):
    i=i+1
    prime = j
  j=j+2
print "prime number ",i,"is ", prime
print("--- %s seconds ---" % (time.time() - start_time))
