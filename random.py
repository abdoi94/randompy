import sys
sys.stdout = open("log.txt", "w")

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print('Original:', purse, '\n')

print('there is', purse['candy'], 'Candies in the purse', '\n')

purse['candy'] = purse['candy'] + 2
print('Edited Dict:', purse, '\n')

sys.stdout.close()