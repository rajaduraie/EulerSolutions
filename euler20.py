def get_sum_from_str(x):
  sum = 0
  for i in range(0, len(x)):
    sum = sum + int(x[i])
  return sum
def fact(x):
  factorial = 1
  while(x>1):
    factorial = factorial*x
    x = x-1
  return factorial;

a = str(fact(100))
print (get_sum_from_str(a))
