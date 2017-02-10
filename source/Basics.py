def createObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if not os.path.isfile(filepath):
        file = open(filepath, "w+")
        file.write("")
        file.close()
        g_print("successfully created Object '"+filename+"'", "Object created!")
        return True

    else:
        g_print("File already exists", "Error. (createObj)")
        return False

def addAttr(filename, count, attr):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "a")
        file.write(count+"\t"+attr+"\n")
        file.close()
        return True
    else:
        print("File not found, creating one.")
        createObj(filename)
        addAttr(filename, count, attr)
        return True

def printObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "r")
        for line in file.read().split("\n"):
            print(line)
        file.close()
        return True
    else:
        g_print("File '"+filename+"' not found.", "Error. (printObj)")
        return False

def delObj(filename):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        os.remove(filepath)
        g_print("successfully removed Object '"+filename+"'", "deleted Object!")
        return True
    else:
        g_print("File '"+filename+"' not found.", "Error. (delObj)")
        return False

def delAttr(filename, attr):
    filename = filename.lower()
    filepath="objects\\"+filename+".txt"
    if os.path.isfile(filepath):
        file = open(filepath, "r")
        tmp = file.read().split("\n")
        newtmp=[]
        for item in tmp:
            if item == "":
                continue
            itemS = item.split("\t")
            if (len(itemS)==2 and attr not in itemS[1]) or (len(itemS)==3 and attr not in itemS[2]):
                newtmp.append(item)
        file.close()

        file = open(filepath, "w")
        for item in newtmp:
            file.write(item+"\n")
        file.close()
        return True
    else:
        g_print("File '"+filename+"' not found.", "Error. (delAttr)")
        return False
