import sys
sys.stdout = open("log.txt", "w")

#####           #####
## slicing a list  ##
#####           #####

a = [18, 24, 46, 10, 15, 20, 40]
print(a[:2])                        ## Print out 0 to 2 ##
print(a[2:5])                       ## Print out 2 to 5 ##
print(a[0:4])                       ## Print out 0 to 4 ##
print(a[:])                         ## Print out the whole list ##

sys.stdout.close()