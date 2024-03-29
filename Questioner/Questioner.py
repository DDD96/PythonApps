from os import path
from random import randint
from sys import argv

listName = "List.l"

currentPath = path.dirname(path.realpath(argv[0]))

cfgPath = path.join(currentPath, "QuestionerCFG.cfg")

if path.exists(path.join(currentPath, listName)) != True:
    print("There is not any list")
if path.exists(cfgPath) != True:
    f = open(cfgPath, "w+")
    f.close()

listPath = open(path.join(currentPath, listName), "r")

content = listPath.readlines()

used = list()

with open(cfgPath, "r") as cfgFile:
    used = cfgFile.readlines()
    for l in used:
        i = used.index(l)
        used[i] =  l.strip()        

while len(used) != len(content):
    input("Exit to exit or Submit to continue") 
    i = randint(0,len(content) - 1)
    while str(i) in used:
        i = randint(0,len(content) - 1)
    print(content[i])
    used.append(str(i))
    with open(cfgPath, "a+") as cfgFile:
        cfgFile.write(str(i) + "\n")

input("Finished")
