fhand = open('mbot.txt')    #Open txt file
inp = fhand.read()          #Read txt file
print(len(inp))             #Print File text length
print('\n' + inp[:20])      #Print from file start to 20