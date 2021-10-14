import sys
sys.stdout = open("log.txt", "w")

x = ('Glenn', 'Sally', 'James')
print(x[2])
print(x)

for aaa in x:
    print(aaa)

sys.stdout.close()