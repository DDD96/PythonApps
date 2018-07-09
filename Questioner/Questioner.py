from os import path
from random import randint
from sys import argv

listName = "List.l"

currentPath = path.dirname(path.realpath(argv[0]))

cfgPath = path.join(currentPath, "QuestionerCFG.cfg")

if path.exists(path.join(currentPath, listName)) != True:
    print("There is not any list")

listPath = open(path.join(currentPath, listName), "r")

content = listPath.readlines()

with open(cfgPath, "a+") as cfgFile:
    used = cfgFile.readlines()


while True:
    input("Exit to exit or Submit to continue") 
    i = randint(0,len(content) - 1)
    while used.count(str(i)) != 0:
        i = randint(0,len(content) - 1)
    print(content[i])
    used.append(str(i))
    with open(cfgPath, "a+") as cfgFile:
        cfgFile.write(str(i) + "\n")
