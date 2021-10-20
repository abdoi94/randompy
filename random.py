import sys
import re
sys.stdout = open("log.txt", "w")

x = 'My 2 favorite numbers are 420 and 69'
y = re.findall('[0-9]+' ,x)
print(y)

sys.stdout.close()