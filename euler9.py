def check_product(x, y, z):
  if (((x*x)+(y*y)) == (z*z)):
    return 1
  return 0

a = 0
b = 1
c = 1000 - (a+b)
for a in range (1, 499):
  while((a+b) <= 666):
    if (check_product(a, b, c)):
      print "The numbers are %d, %d and %d "%(a, b, c)
      print "The product is %d"%(a*b*c)
      break
    b = b+1
    c = 1000 - (a+b)
  b = a+1
  c = 1000 - (a+b)
