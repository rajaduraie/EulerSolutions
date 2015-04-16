import sys
import math
import time

def is_prime (x):
  if ( x == 1):
    return 0
  if (x % 2 == 0):
    return 0
  if (x == 3 ):
    return 1
  if (x < 9):
    return 1
  sqrt_x = int(math.sqrt(x))
  f = 5
  while (f <= sqrt_x ):
    if ( x % f == 0):
      return 0
    if ( x % (f+2) == 0):
      return 0
    f = f+6
  print x 
  return 1

start_time = time.time()
x = 2
#num = 600851475143
num = int(sys.argv[1])
found = 0
# Checking this one time would save a number of iterations later
# for all even numbers
if (num % x == 0):
  num = num/x
elif (is_prime(num)):
  print num 
  found = 1
  exit

x = 3

while(found == 0):
  if (num % x == 0):
    num = num/x
  elif (is_prime(num)):
    print num 
    found = 1
    exit
  x = x+2
print "----------- %s is the time taken "%(time.time() - start_time)
