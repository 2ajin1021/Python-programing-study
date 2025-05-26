i = 1
while i<=30:
    if i%3==0:
        i+=1
        continue    
    else:
        print(i, end=',')
        print(i, ',', sep='', end='')
    i+=1