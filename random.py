import sys
import re
sys.stdout = open("log.txt", "w")

s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

sys.stdout.close()