import random, os, sys

file = open(os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "Frasi"), 'r',)
content = list()
used = list()

for line in file.readlines():
    content.append(line)

s = ""

while s != "exit":
    s = input("Exit to exit or Submit to continue") 
    i = random.randint(0,len(content) - 1)
    while used.count(i) != 0:
        i = random.randint(0,len(content) - 1)
    print(content[i])
    used.append(i)
