tot = 0
for i in range(1,334):
    tot = tot+i*3;

for i in range(1,200):
    if(i%3 == 0):
        continue
    tot = tot+i*5
 
print tot
