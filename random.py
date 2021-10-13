import sys
sys.stdout = open("log.txt", "w")

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

sys.stdout.close()