fname = input('Enter the file name: ')
fhand = open(fname)                                              #Open txt file
count = 0                                                             #Define count to use later
for line in fhand:
     if line.startswith('Hello') :                                    #Find line starting with hello
          count = count + 1                                           #Count those lines
print('There was', count, 'subject lines in:\n', fname)               #Print subjects count