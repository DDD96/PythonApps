import sys

commonStr = input("Insert <commons owned> <total commons>\n")
rareStr = input("Insert <rares owned> <total rares>\n")
epicStr = input("Insert <epics owned> <total epics>\n")
legendaryStr = input("Insert <legendaries owned> <total legendaries>\n")
golden = bool(input("Golden?\n"))
golden = False

commons, totalCommons = (commonStr.split(maxsplit= 1))
rares, totalRares = (rareStr.split(maxsplit= 1))
epics, totalEpics = (epicStr.split(maxsplit= 1))
legendaries, totalLegendaries = (legendaryStr.split(maxsplit= 1))

commons = int(commons)
totalCommons = int(totalCommons)
rares = int(rares)
totalRares = int(totalRares)
epics = int(epics)
totalEpics = int(totalEpics)
legendaries = int(legendaries)
totalLegendaries = int(totalLegendaries)

commons = min(commons, totalCommons)
rares = min(rares, totalRares)
epics = min(epics, totalEpics)
legendaries = min(legendaries, totalLegendaries)

if golden != True:
    pCommons = (1 - commons/totalCommons)*(96.3)/100
    pRares = (1 - rares/totalRares)*(20)/100
    pEpics = (1 - epics/totalEpics)*(4.2)/100
    pLegendaries = 4.19/100
else:
    pCommons = (1 - commons/totalCommons)*(1.5)/100
    pRares = (1 - rares/totalRares)*(1.33)/100
    pEpics = (1 - epics/totalEpics)*(0.25)/100
    pLegendaries = 0.1/100

print("\nCommons Perc: " + str(round(pCommons*100,2)) + "%")
print("Rares perc: " + str(round(pRares*100,2)) + "%")
print("Epics perc: " + str(round(pEpics*100,2)) + "%")
print("Legendaries perc: " + str(round(pLegendaries*100,2)) + "%\n")

input()
