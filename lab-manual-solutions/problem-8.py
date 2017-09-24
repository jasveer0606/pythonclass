from tkinter import *
window = Tk()
window.geometry("500x450")
window.title("Phonebook")
nameL = Label(window,text="Name:").place(x=140,y=20)
phoneL = Label(window,text="Phone:").place(x=140,y=50)
nameE = Entry(window,width=25)
phoneE = Entry(window,width=25)
nameE.place(x=190,y=20)
phoneE.place(x=190,y=50)
db = {}
frame = Frame(window)
scrollbar = Scrollbar(frame, orient=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=18)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)
def add():
    db[nameE.get()] = phoneE.get()
    nameE.delete(0,END)
    phoneE.delete(0,END)
    load()
def load():
    listbox.delete(0,END)
    for i in sorted(list(db)):
        listbox.insert(END,"  :  ".join([i,db[i]]))
addB = Button(window,width=12,text="Add",command=add)
updateB = Button(window,width=12,text="Update",command=add)
deleteB = Button(window,width=12,text="Delete",command=lambda lb=listbox:lb.delete(ANCHOR))
loadB = Button(window,width=12,text="Load")
addB.place(x=20,y=80)
updateB.place(x=140,y=80)
deleteB.place(x=260,y=80)
loadB.place(x=380,y=80)
frame.place(x=120,y=125)

















window.mainloop()
