import sys
sys.stdout = open("log.txt", "w")

########            #######
## Print out List length ##
########            #######

friends = ['Ali', 'Saif', 'Ahmed']
print(len(friends))

sys.stdout.close()