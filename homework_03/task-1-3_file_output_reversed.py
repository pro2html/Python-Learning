import sys

list = []

filename = sys.argv[1]
f = open(filename, 'r')

for line in f:
    list.append(line)
f.close()

list.reverse();

for i in range(0, len(list)):
    print(list[i])