def get_sum_from_str(x):
  sum = 0
  for i in range(0, len(x)):
    sum = sum + int(x[i])
  return sum
x = str(2**1000)
print(get_sum_from_str(x))
