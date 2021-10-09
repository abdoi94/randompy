import sys
sys.stdout = open("log.txt", "w")

########                  ########
## Print out all Items in a list##
########                  ########
list = [5, 4, 3, 2, 1]
for i in list:
     print(i)
print('Lets go! \n')


########                             ########
## Print out a text with Items from a list ##
########                             ########

z = ['Ali', 'Saif', 'Ahmed']
for x in z:
     print('Happy Eid:', x)
print('Done! \n')

sys.stdout.close()