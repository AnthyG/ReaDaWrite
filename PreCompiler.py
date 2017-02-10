import os

sourcedir="source\\"

global output
output = ""

def rFile(fileP):
    fileO = open(fileP, "r")
    fileR = fileO.read()
    fileO.close()
    return fileR

def addIt(file, fileR):
    global output
    print("Adding " + file)
    output += "\n\n#---\n#" + file + "\n#---\n\n" + fileR

#Import MainTop.py as first Module
addIt("MainTop.py", rFile(sourcedir+"MainTop.py"))

#Import all modules except MainTop.py and MainBot.py
for file in os.listdir(sourcedir):
    if file.endswith(".py") and file!="MainTop.py" and file!="MainBot.py":
        addIt(file, rFile(sourcedir+file))

#Import MainBot.py as last Module
addIt("MainBot.py", rFile(sourcedir+"MainBot.py"))

fileW = open("KI.py", "w")
fileW.write(output)
fileW.close()
