import sys
sys.stdout = open("log.txt", "w")

counts = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }

for key in counts:            ## print keys with their values
    print(key, counts[key])

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

sys.stdout.close()