
def check (x, y):
  if( x%y == 0):
    return 1
  return 0

def is_prime (x):
  if (x % 2 == 0):
    return 0
  i = 3
  while (i <= int(x/2)):
    if (x % i == 0):
      return 0
    i = i + 2
  return 1

x = 2520
y = 1
while (y < 21):
  if ( check(x, y)):
    print "%d is divisible " %(y)
  else:
    while(not check(x, y)):
      if (is_prime(y)):
        x = x * y
      else:
        j = 2
        while(not check(x*j, y)): 
          j = j + 1
        x = x * j
  y = y + 1     
  
print x
