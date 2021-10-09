import sys
sys.stdout = open("log.txt", "w")

########        #######
## Concatenate lists ##
########        #######

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

sys.stdout.close()