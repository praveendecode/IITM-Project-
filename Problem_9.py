# create option button using tkinter GUI in python
from tkinter import *

window = Tk()

list_option = ["Hey create your own option","Why are you looking second option ","Again  you looking Third option "]
label = Label(text="Who are you ?",fg="white",bg="green",font=("times new roman",60,"bold"))
label.pack()
for i in range(len(list_option)):
    option_button = Button(text=list_option[i],font=("times new roman",20,"bold"),bd=3,relief=GROOVE)
    option_button.pack()




window.mainloop()
