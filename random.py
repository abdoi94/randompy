import sys
sys.stdout = open("log.txt", "w")

numlist = list()
while True :
     inp = input('Please Enter a number: \n')
     if inp == 'done' : break
     value = float(inp)
     numlist.append(value)

average = sum(numlist) / len(numlist)
print('\nAverage:', average)

sys.stdout.close()