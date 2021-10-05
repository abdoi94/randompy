smallest = -1
print('Before', smallest)
for num in [9, 41, 12, 3, 74, 15]:
    if num < smallest:
        smallest = num
        print(smallest, num) 
print('After', smallest)
