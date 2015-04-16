import sys

def palindrom(c,d):
    z= 0
    for i in range(c,100,-1):
    	for j in range (d, 100, -1):
    		mul = j*i
    		if (comp(mul) == 1):
    			if mul > z:
    				print (j)
    				print (i)
    				z = mul
    print (z)
   

           		              	

        
       
                    
def comp (y):
    y_str = str(y)
    y_str = y_str[::-1]
    if (y == int(y_str)):
        return 1
    else :
        return 0 
        
palindrom(int(sys.argv[1]), int(sys.argv[2]))
