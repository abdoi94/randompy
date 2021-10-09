import sys
sys.stdout = open("log.txt", "w")

#####         #####
## build a list  ##
#####         #####

stuff = list()
stuff.append('book')
stuff.append('99')
stuff.append('cookie')
print(stuff)


#####        #####
## Sort a list  ##
#####        #####

sorted = stuff
sorted.sort()
print(sorted)
print(sorted[1])


sys.stdout.close()