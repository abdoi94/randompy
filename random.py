import sys
sys.stdout = open("log.txt", "w")

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

sys.stdout.close()