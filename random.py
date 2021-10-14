import sys
sys.stdout = open("log.txt", "w")

b = {'a':10, 'b':1, 'c':22}
t = sorted(b.items())
for k, v in t:
    print(k, v)

sys.stdout.close()