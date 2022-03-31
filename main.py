
import os
import itertools

print ( "Gathering the system resource information........\n ==============#################===============" )

data = os.system(" echo '' > mydata.txt; for i in `cat servers.txt`;do ssh  ubuntu@$i 'hostname && sudo sh /etc/update-motd.d/50-landscape-sysinfo' ; echo '====='; done | tee mydata.txt ")

print(" Fetching the current memory utilisation..........\n")

print("==============#################===============")

os.system("cat mydata.txt|grep Memory")

print("==============#################===============")

print("Sorting algorithm -- preparing the list as per lowest first............\n")

os.system("cat mydata.txt | grep Memory | cut -d 'I' -f1| sort | tee Memory.txt")

print("==============#################===============")

print("Starting the algorithm, choosing the population..............\n")

os.system("cat servers.txt")

print("\n==============#################===============")

print("Iteration - 1 ................. Starting\n ")
print("First Generation - Parents...........\n")

population = os.system("cat servers.txt |wc -l")

print("The hosts in the selected population is: {} ".format(population))

print("==============#################===============")

print("Dividing the population into tournament participants ...........\n")

#os.system("cat Memory.txt|cut -d "IPv" -f1 > Memory.txt")

for i, j in itertools.zip_longest(range(0, 10, 2), range(1,10,2)):
    with open("Memory.txt") as f:
     firstline = f.readlines()[i].rstrip()
    with open("Memory.txt") as f:
     secondline = f.readlines()[j].rstrip()

    print(firstline)
    print(secondline)

    print ("======================")

    print ("Running tournament --> iteration 1")
    if firstline>secondline:
      print("Number {} is greater than Number {}".format(i, j))
    elif firstline<secondline:
      print("Number {} is less than Number {}".format(i, j))
    else:
     print("Number1 is equal to Number2")

    print ("==========================================")

