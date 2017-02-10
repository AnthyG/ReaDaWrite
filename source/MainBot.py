##def getRawAttrList(filename):
##    arr=[]
##    filename = filename.lower()
##    filepath="objects\\"+filename+".txt"
##    if os.path.isfile(filepath):
##        file = open(filepath, "r")
##        for line in file.read().split("\n"):
##            arr.append(line.split("\t")[1])
##        file.close()
##    else:
##        print("File '"+filename+"' not found.")
##    return arr

def main():
    global lastObj, usegui
    try:
        inp = clearArr(g_input("Your CMD > ", "Input").split(" "))
        
        if not lastObj=="":
            inp.insert(1, lastObj)
        if inp==[] or inp[0]=="listObjs":
            x = os.listdir("objects\\")
            for item in x:
                print(item)
        elif inp[0]=="addAttr":
            x = addAttr(inp[1], "a", inp[2])
            if not x:
                print("something went wrong")
            else:
                printObj(inp[1])
                
        elif inp[0]=="createObj":
            x = createObj(inp[1])
            if not x:
                print("something went wrong")
                
        elif inp[0]=="delObj":
            x = delObj(inp[1])
            if not x:
                print("something went wrong")
                
        elif inp[0]=="printObj":
            x = printObj(inp[1])
            if not x:
                print("something went wrong")
    
        elif inp[0]=="setObj" and len(inp)==2:
            lastObj = inp[1]
    
        elif inp[0]=="addFromText":
            x = g_input("[German] Bitte einen Satz eingeben: ")
            dataFromSentences(x)
    
        elif inp[0]=="useTXT":
            if len(inp) == 2:
                dataFromTXT(inp[1])
            else:
                dataFromTXT()
        
        elif inp[0] == "sgui":
            if usegui:
                usegui = False
            else:
                usegui = True
            print("Switched gui-mode to " + str(usegui))
        
        elif inp[0] == "help":
            helpPrint()
            main()
            return
        
        elif inp[0] == "exit":
            sys.exit()
            
    except AttributeError:
        usegui = False
    
    clearObjs()
    main()

def helpPrint():
    helpstring = """
Prints this: 'help'
List all Objects: 'listObjs'
Create Object: 'createObj [obj]'
Print Object: 'printObj [obj]'
Delete Object: 'delObj [obj]'
Add Adjective: 'addAttr [obj] <attribute>'
Delete Attribute: 'delAttr [obj] <attribute>'
Automatically Filter new Data: 'addFromText'
Take Data out of a file: 'useTXT [filename]'
Set Object: 'setObj <obj>'
Sets [obj] to default to <obj>
Exit the program: 'exit'"""
    print(helpstring)
    
    if usegui:
        choice = eg.choicebox("Available commands", "Help", clearArr(helpstring.split("\n")))

def firstStart():
    if not os.path.exists("objects\\"):
        os.makedirs("objects\\")
        
    helpPrint()
    
    main();
    
firstStart()
