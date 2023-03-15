from tkinter import *

r="аисъбйтывкуьглфэдмхюенцяёочжпшзрщ"
num="111122223333444455556666777888999"
r1="ajsbktcludmvenwfoxgpyhqzir"
num1="11122233344455566677788899"

def kontrol():
    a=entname.get() 
    if a.isalpha()==False or len(a)<2:
        entname.configure(bg="Red")
        x=False
        f=0
    else:
        entname.configure(bg="Grey")
        x=True
        f=a.lower().translate(a.maketrans(r,num)).translate(a.maketrans(r1,num1))
        while len(list(str(f)))!=1:
            f=list(map(int,list(str(f))))
            f=sum(f)
    return x,f

def watch(event):
    x,f=kontrol()
    win1=Tk()
    win1.geometry("1920x1080")
    win1.title("Numeroloogia arv")
    with open(f"tfile{f}.txt","r",encoding="utf-8-sig") as y:
        jarjend=""
        for rida in y:
            jarjend+=rida.strip()+"\n"
    print(jarjend)
    lbltext=Label(win1,text=jarjend,font="Arial 20",fg="black")
    lbltext.pack()

def numog(event):
    x,f=kontrol()
    if x==True:
        lblnum.configure(text=f"Sinu arv - {f}")
        btnwatch=Button(win,text="Vaadake numbri väärtust",font="Arial 20",fg="Black",bg="Gray")
        btnwatch.pack(side=BOTTOM)
        btnwatch.bind("<Button-1>",watch)

win=Tk()
win.geometry("600x400")
win.title("Numeroloogia arv")

lbl=Label(win,text="Numeroloogia arv",font="Arial 40",fg="black")
entname=Entry(win,fg="Black",justify=CENTER,bg="Grey",font="Arial 20",width=15)
btnname=Button(win,text="Sisenema",font="Arial 20",fg="Black",bg="Gray")
lblnum=Label(win,text="",font="Arial 20",fg="black")

btnname.pack(side=BOTTOM,pady=10)
lbl.pack()
lblnum.pack()
entname.pack(side=BOTTOM,pady=80)

btnname.bind("<Button-1>",numog)

win.mainloop()