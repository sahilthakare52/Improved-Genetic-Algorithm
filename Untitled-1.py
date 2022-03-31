import itertools


for i, j in itertools.zip_longest(range(0, 10, 2), range(1,10,2)):
    print(i)
    print(j)
    
   
