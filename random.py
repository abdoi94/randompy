import sys
sys.stdout = open("log.txt", "w")

counts = dict()
line = input('Enter a line of text:')
words = line.split()
print('Words:', words)
print('\nCounting...\n')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

sys.stdout.close()