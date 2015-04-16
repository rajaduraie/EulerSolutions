import sys

def fib(x):
    a,b = 0,1
    even_total = 0
    while(a<x) :
        a,b = b, a+b
        if (a % 2 == 0):
            even_total += a
    return even_total
total = fib(int(sys.argv[1]))
print total
