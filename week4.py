with open('data.txt', 'w') as f:
    for i in range(101):
        f.write(f"{i},{i**2}\n")

with open('data.txt', 'a') as f:
    for i in range(101,151):
        f.write(f"{i},{i**2}\n")

with open('data.csv', 'w') as f:
    for i in range(101):
        f.write(f"{i},{i**2}\n")

import os
os.startfile('data.csv') # windows only

import os
os.startfile('data.txt') # windows only

with open('data.txt', 'r') as f:
    content = f.read()
    print(content)

x_values = []
y_values = []
with open('data.txt', 'r') as f:
    next(f)  # (optionally - to skip header line)
    for line in f:
        x, y = line.strip().split(',')
        x_values.append(int(x))
        y_values.append(int(y))
print(x_values)
print(y_values)