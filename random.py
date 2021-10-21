import socket
import sys
sys.stdout = open("log.txt", "w")

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.py4e.com', 80))
print(mysock)
sys.stdout.close()