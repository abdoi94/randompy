import sys
sys.stdout = open("log.txt", "w")

(x, y) = ('4', 'James')
print(x)

(a, b) = ('21', 'Madison')
print(b)

sys.stdout.close()