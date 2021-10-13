import sys
sys.stdout = open("log.txt", "w")

counts = dict()
names = ['csev', 'cwen', 'gwem', 'csev', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

sys.stdout.close()