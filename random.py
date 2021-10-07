fhand = open('mbot.txt')    #Open txt file
for line in fhand:
    if line.startswith('Hello') : #Find line starting with hello
        print(line)               #Print those hello lines