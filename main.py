
import os
import itertools

print ( "Gathering the system resource information........\n ==============#################===============" )

data = os.system(" echo '' > mydata.txt; for i in `cat servers.txt`;do ssh  ubuntu@$i 'hostname && sudo sh /etc/update-motd.d/50-landscape-sysinfo' ; echo '====='; done | tee mydata.txt ")

print(" Fetching the current memory utilisation..........\n")

print("==============#################===============")

os.system("cat mydata.txt|grep Memory")

print("==============#################===============")

print("Sorting algorithm -- preparing the list as per lowest first............\n")

#os.system("cat mydata.txt | grep Memory | cut -d 'I' -f1| sort | tee Memory.txt")
os.system("cat mydata.txt | grep Memory | sort | tee Sorted.txt")
#os.system("cat mydata.txt | grep -e 'ip-1' -e 'Memory' | tee servername_with_memory.txt")

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

#os.system("cat Memory.txt|cut -d "I" -f1 > Memory.txt")


os.system("cat mydata.txt | grep Memory | cut -d 'I' -f1| sort | tee Memory.txt >/dev/null 2>&1")

def update_next_iteration(selections):
        fil=open("next_iteration_list.txt", "a")
        fil.write(selections + "\n")
        fil.close

def tourament_func(n):
    for i, j in itertools.zip_longest(range(0, 10, 2), range(1,10,2)):
      with open("Memory.txt") as f:
       firstline = f.readlines()[i].rstrip()
      with open("Memory.txt") as f:
       secondline = f.readlines()[j].rstrip()
       print(firstline)
       print(secondline)

       print ("======================")

       print ("Running tournament --> iteration {}".format(n))
       if firstline>secondline:
          print("Memory  utilisation for server {} is greater than server {}\n Server {} is selected".format(i, j, j))
          update_next_iteration(secondline)
       elif firstline<secondline:
          print("Memory  utilisation for server {} is less than server {}\n Server {} is Selected ".format(i, j, i))
          update_next_iteration(firstline)
       else:
          print("Memory  utilisation for server {} is equal to server {}\n Server will be selected randomly".format(i, j))
          update_next_iteration(firstline)
       print ("==========================================")
 
tourament_func(1)


