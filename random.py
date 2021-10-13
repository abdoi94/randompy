import sys
sys.stdout = open("log.txt", "w")

counts = { 'chuck' : 1 , 'fred' : 42 , 'jan' : 100 }

for aaa,bbb in counts.items():         
    print(aaa, bbb)

sys.stdout.close()