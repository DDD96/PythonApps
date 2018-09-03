import sys
import time
from tkinter import *

tCommons = 1
tRares = 1
tEpics = 1
tLegendaries = 1
pCommons = 1
pRares = 1
pEpics = 1
pLegendaries = 1   

def CalcProb():

    cCardSet = sEntry.get()

    if cCardSet == "TGT" or cCardSet == "MSG":
        tCommons = 98
        tRares = 72
        tEpics = 54
        tLegendaries = 20
    elif cCardSet == "GvG":
        tCommons = 80
        tRares = 74
        tEpics = 52
        tLegendaries = 20
    elif cCardSet == "TW" or cCardSet == "KaC" or cCardSet == "KFT" or cCardSet == "UNG":
        tCommons = 98
        tRares = 72
        tEpics = 54
        tLegendaries = 23
    elif cCardSet == "Gods":
        tCommons = 100
        tRares = 72
        tEpics = 54
        tLegendaries = 21
    elif cCardSet == "Classic":
        tCommons = 182
        tRares = 158
        tEpics = 70
        tLegendaries = 31
    elif cCardSet == "BOOM":
        tCommons = 98
        tRares = 72
        tEpics = 54
        tLegendaries = 23
    else:
        print("Error: No set")

    commons = int(cEntry.get())
    rares = int(rEntry.get())
    epics = int(eEntry.get())
    legendaries = int(lEntry.get())

    commons = min(commons, tCommons)
    rares = min(rares, tRares)
    epics = min(epics, tEpics)
    legendaries = min(legendaries, tLegendaries)

    if golden.get() != True:
        pCommons = (1 - commons/tCommons)*(99.92)/100
        pRares = (1 - rares/tRares)*(95.66)/100
        pEpics = (1 - epics/tEpics)*(20.56)/100
        pLegendaries = 5.13/100
    else:
        pCommons = (1 - commons/tCommons)*(1.5*5)/100
        pRares = (1 - rares/tRares)*(1.33*5)/100
        pEpics = (1 - epics/tEpics)*(0.25*5)/100
        pLegendaries = (0.1)*5/100

    cPerc.configure(text = "Commons Perc: " + str(round(pCommons*100,2)) + "%")
    rPerc.configure(text = "Rares perc: " + str(round(pRares*100,2)) + "%")
    ePerc.configure(text = "Epics perc: " + str(round(pEpics*100,2)) + "%")
    lPerc.configure(text = "Legendaries perc: " + str(round(pLegendaries*100,2)) + "%")
    totPerc.config(text = "Total perc:" + str(round(min(pCommons + pRares + pEpics + pLegendaries, 1)*100,2)) + "%")


app = Tk(className=" Hs Probability")


#Commons Entry
Label(app, text = "Commons: ").grid(row = 0, column = 0, ipady = 5)

cEntry = StringVar() 
cEntry.set("0")
Entry(app, textvariable = cEntry).grid(row = 0, column = 1)

#Rares Entry
Label(app, text = "Rares: ").grid(row = 1, column = 0, ipady = 5)

rEntry = StringVar()
rEntry.set("0")
Entry(app, textvariable = rEntry).grid(row = 1, column = 1)

#Epics Entry
Label(app, text = "Epics: ").grid(row = 2, column = 0,ipady = 5)

eEntry = StringVar()
eEntry.set("0")
Entry(app, textvariable = eEntry).grid(row = 2, column = 1)

#Legendary Entry
Label(app, text = "Legendaries: ").grid(row = 3, column = 0, ipady = 5)

lEntry = StringVar()
lEntry.set("0")
Entry(app, textvariable = lEntry).grid(row = 3, column = 1)

#Card Set Option

optionList = list(["Classic", "GvG", "TGT", "Gods", "MSG", "UNG", "KFT", "KaC", "TW", "BOOM"])

sEntry = StringVar()
sEntry.set(optionList[0])

Label(app, text = "Card set: ").grid(row = 4, column = 0, ipady = 5)
OptionMenu(app, sEntry, *optionList).grid(row = 4, column = 1)

#Golden CheckButton

golden = BooleanVar()

Checkbutton(app, text = "Golden?", variable = golden).grid(row = 5)

cPerc = Label(app)
cPerc.grid(row = 0, column = 3, ipadx = 35)
rPerc = Label(app)
rPerc.grid(row = 1, column = 3)
ePerc = Label(app)
ePerc.grid(row = 2, column = 3)
lPerc = Label(app)
lPerc.grid(row = 3, column = 3)
totPerc = Label(app)
totPerc.grid(row = 4, column = 3)

#Calculate Button

Button(app, text = "Calculate", command = CalcProb).grid(row = 5, column = 3)

app.mainloop()


