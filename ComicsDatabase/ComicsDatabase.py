from tkinter import Label,Button,Entry,StringVar,OptionMenu,Tk,sys
import os

#Instantiate Panel
main = Tk(className="Topolino")
main.geometry("800x250")

#Get Path
path = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "Fumetti.comics")

def SortFile():
    lines = dict()

    file = open(path, "r")
    #Make dictionary (Series, List(Number))
    for line in file.readlines():
        ser,num = line.split("-")
        num = num.strip()
        num = int(num)
        if ser in lines:
            lines[ser].append(num)
        else:
            lines[ser] = [num]
    #Sort the list in dictionary
    for key, value in lines.items():
        lines[key] = sorted(value)
    file.close()

    newdic = dict()
    for key in sorted(lines.keys()):
        newdic[key] = lines[key]

    os.remove(path)

    file = open(path, "w")
    #Print ordered files
    for key, value in newdic.items():
        for num in value:
            file.write(key + "-" + str(num) + "\n")
    file.close()

    evaluationString.set("Sorted")

def AddComic():
    collana = GetCollana()

    if collana == "":
        return

    if textNum.get().isdigit() == False:
        evaluationString.set("Number must be a DIGIT not " + textNum.get())
        ValidateNumber()
        return

    Search()

    if evaluationString.get() == "Present":
        return

    file = open(path,"a")
    file.write(collana.get() + "-" + textNum.get() + "\n")
    file.close()

    evaluationString.set(collana.get() + "-" + textNum.get() + " ADDED")

def GetCollana():
    if collana1.get() != "":
        return collana1
    elif collana2.get() != "":
        return collana2
    else:
        return ""

def Search():
    collana = GetCollana()

    if collana == "":
        return

    file = open(path, "r")
    for line in file.readlines():
        series, num = line.split("-")
        num = num.strip()
        if((series == collana.get()) & (num == textNum.get())):
            evaluationString.set("Present")
            return
    evaluationString.set("Not present")
    file.close()

def ValidateNumber():
    num = textNum.get()
    if num.isdigit() == False:
        textNum.set("0")

#First Line
Label(main, text = "Collana").grid(row = 0, column = 0, padx = 10)

optionList1 = list(["","Topolino", "Disney Big", "Disney Time", "Disney Comics", "I Grandi Classici(II serie)",
"Mega Almanacco", "Paperadamus", "Paperinik", "Paperino Mese", "Più Disney", "Speciale Disney", "Super Disney", "Super Miti Mondadori",
"Topo goal", "Tutto Disney", "I Grandi Classici", "I Classici di Walt Disney (II serie)", "I Miti Mondadori", "Zio Paperone", "Disney Happy",
"Le più belle storie Disney", "Le più belle storie Disney special", "Paperstyle", "La Storia Universale Disney", "Capolavori della Letteratura",
"Topostorie Disney"])
optionList1.sort()

optionList2 = list(["","Disney Definitive Collection", "Disney Legendary Collection", "I Mitici Disney", "Virtù e difetti a fumetti",
"Un pieno di avventure", "Topolino Story", "La grande dinastia dei paperi", "L'altro Topo", "Le grandi storie Disney L'opera omnia di Romano Scarpa",
"Tesori Made in Italy", "Tesori Disney International", "L’economia di Zio Paperone", "The Don Rosa library Zio Paperone & Paperino",
"Astromondi di Topolino", "Disney Comix", "Paperdinastia (Giunti)", "I Classici della Letteratura", "I Classici della Letteratura (2a edizione)",
"Zio Paperone (Panini)"])
optionList2.sort()

collana1 = StringVar()
collana1.set(optionList1[1])

OptionMenu(main, collana1, *optionList1).grid(row = 0, column = 1)

collana2 = StringVar()
collana2.set(optionList2[0])

OptionMenu(main, collana2, *optionList2).grid(row = 0, column = 2)

Label(main, text = "Numero").grid(row = 0, column = 3, padx = 10)

textNum = StringVar()
textNum.set("0")

Entry(main, textvariable = textNum, validate = "all", validatecommand = ValidateNumber).grid(row = 0, column = 4)

#Second Line

Button(main, text = " "*3 + "Add" + " "*3, command = AddComic).grid(row = 2, column = 1, pady = 10)

Button(main, text = "Search", command = Search).grid(row = 2, column = 3)

Button(main, text = "Sort", command = SortFile).grid(row = 2, column = 2)

#Third Line

evaluationString = StringVar()
evaluationString.set("Not present")

Label(main, textvariable = evaluationString).grid(row = 3, column = 2, pady = 10)

#Loop

main.mainloop()
