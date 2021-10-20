import sys
import re
sys.stdout = open("log.txt", "w")

hand = open('words.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

sys.stdout.close()