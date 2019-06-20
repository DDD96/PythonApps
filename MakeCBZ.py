#!/usr/bin/python3

from glob import glob
from os.path import join, dirname, abspath
from os import rename
from subprocess import Popen, run
from zipfile import ZipFile

folderName = input("Insert folder name: ")
pages = input("Insert number of pages: ")

if(pages.isdecimal() == False or int(pages) > 2 or int(pages) < 0):
    exit(-1)

currFolder = dirname(abspath(__file__))


files = glob(join(folderName, "*.jpg"))
count = 0

files.sort()


Popen(["mogrify -resize " + str(1169*int(pages)) + "x1700! -quality 75 \"" + join(folderName, "*.jpg\"")], shell=True).wait()

print("Converted")

for f in files:
    name = join(folderName, str(count).zfill(3) + ".jpg")
    rename(f, name)
    count += 1


zipFile = ZipFile(folderName + ".cbz", mode="w")

for i in range(0, count):
    zipFile.write(join(folderName, str(i).zfill(3) + ".jpg"), arcname=str(i) + ".jpg")

zipFile.close()

input("Compressed")
