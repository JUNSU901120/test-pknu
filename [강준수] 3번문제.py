from tkinter import *
window = Tk()

def  rdo_change() :
    if var.get() == 1 :
        label1.configure(text = "벤츠")
    else :
        label1.configure(text = "포르쉐")
    
var = IntVar()
rb1 = Radiobutton(window, text = "벤츠", variable = var, value = 1, command = rdo_change)
rb2 = Radiobutton(window, text = "포르쉐", variable = var, value = 2, command = rdo_change)


label1 = Label(window, text="선택한 차량 : ", fg="red")

rb1.pack()
rb2.pack()
label1.pack()

window.mainloop()
