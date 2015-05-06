f = open('numbers.txt', 'r')
sum = 0
for line in f:
  a = line.rstrip()
  sum = sum + int(a)
  print( sum )

sum = str(sum)
print (sum[0:10])
