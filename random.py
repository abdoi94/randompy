import sys
import re
sys.stdout = open("log.txt", "w")

hand = open('words.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)

sys.stdout.close()