import os
import itertools

population = os.system("cat servers.txt |wc -l")



for i, j in itertools.zip_longest(range(0, 10, 2), range(1,10,2)):
    with open("Memory.txt") as f:
     firstline = f.readlines()[i].rstrip()
    with open("Memory.txt") as f:
     secondline = f.readlines()[j].rstrip()

 #   print(firstline)
 #   print(secondline)
    if firstline>secondline:
      print("Number {} is greater than Number {}".format(i, j))
    elif firstline<secondline:
      print("Number {} is less than Number {}".format(i, j))
    else:
     print("Number1 is equal to Number2")

    print ("==========================================")