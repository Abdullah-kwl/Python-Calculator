from tkinter import *


def perform(event):
    
    # global scvar
    text=event.widget.cget("text")

    if text=="=":
        if scvar.get().isdigit():
            value=int(scvar.get())
        else:
            try:
                value=eval(scvar.get())
            except Exception as e:
                print(e)
                value="Error"
        
        scvar.set(value)

    elif text=="C":
        scvar.set("")
        screen.update()
    else:
        scvar.set(scvar.get()+text)
        screen.update()

# ========================================================================

root=Tk()
root.geometry("350x500")
root.maxsize(350,500)
root.minsize(350,500)
root.title("Abdullah's Calculator")
root.configure(background='grey')
root.wm_iconbitmap("5.ico") 


# ==============================================================================

scvar=StringVar()
scvar.set("")
screen=Entry(root,font=("lucida", 25,"bold"),bd=10,bg="#88bbeb",relief=SUNKEN,textvar=scvar)
screen.pack(padx=10,pady=20)

# ===============================================================================

f=Frame(root,bg="grey",padx=10,pady=10)

b=Button(f,text="9",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="8",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="7",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="C",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

f.pack()


# ========================================================================

f=Frame(root,bg="grey",padx=10,pady=10)

b=Button(f,text="6",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="5",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="4",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="*",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

f.pack()

# ========================================================================

f=Frame(root,bg="grey",padx=10,pady=10)

b=Button(f,text="3",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="2",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="1",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="/",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

f.pack()


# ========================================================================

f=Frame(root,bg="grey",padx=10,pady=10)

b=Button(f,text="0",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="+",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="-",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

b=Button(f,text="=",padx=10,pady=10,bd=5,bg="#88bbeb",font=("lucida", 20,"bold"))
b.pack(side="left",padx=10)
b.bind("<Button-1>", perform)

f.pack()

# ========================================================================




root.mainloop()


