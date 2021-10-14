import sys
sys.stdout = open("log.txt", "w")

d = dict()
d['csev'] = 4
d['cwen'] = 8
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

sys.stdout.close()