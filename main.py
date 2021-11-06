# Omar alashqar
# 1565085

#
#
# CODE IS NOT FULLY FINISHED
#
#

# IMPORTING ALL APPROPRIATE CLASSES
import copy
import csv
from operator import itemgetter
from datetime import datetime
import random

ManufacturerFile = input()

PriceFile = input()

SdFile = input()

## OPEN MANUFACTURER FILE AND READ ITS CONTENTS
with open(ManufacturerFile) as manfile:
    ListReader = csv.reader(manfile)
    ManufacturerList = []
    isDamagedList = []

    for row in ListReader:
        ManufacturerList += [row]
        manList = ManufacturerList
    i = 0

    ## APPENDS 'damaged' elments to isDamagedList

    while i < len(manList):
        val = manList[i].pop(3)
        isDamagedList.append(val)
        i += 1



    pricesOnlyList = []

with open(PriceFile) as pfile:
    ListReader = csv.reader(pfile)
    PricesList = []

    for row in ListReader:
        PricesList += [row]
    pList = PricesList


    ## APPENDS PRICES TO FULL INVENTORY
    i = 0
    while i < len(manList):
        n = 0
        while n < len(pList):
            if manList[i][0] == pList[n][0]:
                manList[i].append(pList[n][1])
            n += 1
        i += 1




    datesList = []

with open(SdFile) as sdFile:
    ListReader = csv.reader(sdFile)
    SdList = []

    for row in ListReader:
        SdList += [row]
        sList = SdList
    ## APPENDS SERVICE DATES TO FULL INVENTORY
    i = 0
    while i < len(manList):
        n = 0
        while n < len(sList):
            if manList[i][0] == sList[n][0]:
                manList[i].append(sList[n][1])
            n += 1
        i += 1





    ## ADDS THE DAMAGED CONTENT TO THE END OF THE FULL INVENTORY
    n = 0
    while n < len(isDamagedList):
        manList[n].append(isDamagedList[n])
        n += 1

    FullInventoryList = []
    ## SORTS THE FULL INVENTORY LIST BY MANUFACTURER
    FullInventoryList = (sorted(manList, key=(itemgetter(1))))
    ## WRITES INTO THE FULLINVENTORY CSV TO COMPLETE PART A
    with open('FullInventory.csv', 'w', newline='') as fullFile:
        FileWriter = csv.writer(fullFile)

        for row in FullInventoryList:
            FileWriter.writerow(row)





    ## PART B --- DOES NOT WORK -- UNFINIHSED

    J = copy.deepcopy(FullInventoryList)

    hd = []
    i = 0



    s = 0
    while s < len(FullInventoryList):
           val2 = J[s].pop(2)
           hd.append(val2)
           s += 1


    hd = list(set(hd))
   # print(hd)

    rList = ['a', 'b', 'c', 'd', 'e']
    ranList = random.choice(rList)









    ## PART C
    ##          DOES NOT WORK  --- UNFINISHED
    svdList = []
    svdList = FullInventoryList.copy()

    date1 = datetime.today()
    i = 0


    ## PART D
    dmglist = []
    dmglist = FullInventoryList.copy()
    damagedList = []
    i = 0
    ## Loop to find if the contents of dmgList which is a copy of Fullinventory are equal to 'damaged'
    while i < len(FullInventoryList):
        if dmglist[i][5] == 'damaged':
            damagedList.append(dmglist[i])
        i += 1
        # sort to put the damage list in most expensive to least
    damagedList = sorted(damagedList, key=(itemgetter(3)), reverse=True)

    # code to write them to the proper file
    with open('DamagedInventory.csv', 'w', newline='') as dmgFile:
        fileWriter = csv.writer(dmgFile)

        for row in damagedList:
            fileWriter.writerow(row)



