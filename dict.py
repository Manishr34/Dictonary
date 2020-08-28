from tkinter import *
from PyDictionary import PyDictionary

main = Tk()

def defi():
    word = entry.get()
    dic = PyDictionary()
    meaning = dic.meaning(word)
    out["text"]=meaning
    
main.title("Dictionary")
title = Label(text="Dictionary",font=("Ariel",18,"bold"),fg = "green")
title.pack()
root=Frame(main)
root.pack()
lbl = Label(root,text="Enter a Word",font=("times"),pady=8,padx =8)
lbl.grid(row=0,column=0)
entry = Entry(root,font=("times",15,"bold"))
entry.grid(row=0,column=1)
btn = Button(root,text="Defination",command=defi,bd=1,fg="white",bg="black",width=15,pady=8)
btn.grid(row=1,column=1)
out = Label(root,pady=8,fg="green",bg = "light blue")
out.grid(row=2,column=1)
main.geometry("600x300")
main.mainloop()
