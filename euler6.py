import sys

def add_seq(x):
	sum_seq = 0
	for i in range(1, x+1, 1):
		sum_seq = sum_seq+i
	return sum_seq
	
def add_sqr(x):
	sum_sqr = 0
	for i in range (1, x+1, 1):
		sum_sqr = sum_sqr + (i*i)
	return sum_sqr

sum_seq = add_seq(int(sys.argv[1]))
sum_seq_sqr = sum_seq*sum_seq
sum_sqr = add_sqr(int(sys.argv[1]))

print "Difference is :"
print sum_seq_sqr - sum_sqr
