def g_print(msg="", title=""):
    if msg == "":
        pass
    print(msg)
    if usegui:
        eg.msgbox(msg, title)
        
def g_input(msg="", title=""):
    if usegui:
        inputed = eg.enterbox(msg, title)
    else:
        inputed = input(msg)
    return inputed
