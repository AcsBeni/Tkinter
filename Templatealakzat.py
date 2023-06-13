from tkinter import *

ablak=Tk()

def ablak3():
    ablak1= Toplevel(ablak)
    txt=Message(ablak1, text="az eredmény:", width=200)
    txt.grid(row=1, column=2)
    gomb2=Button(ablak1, text="kilépés", command=ablak1 and ablak.destroy)
    gomb2.grid(row=2, column=2)
    ablak1.mainloop()

txt2=Label(ablak, text="Alakzat")
txt2.grid(row=1, column=2)
txt3=Label(ablak, text="adott oldal")
txt3.grid(row=2, column=1)
mezo1=Entry(ablak)
mezo1.grid(row=2, column=2)
txt4=Label(ablak, text="Bdott oldal")
txt4.grid(row=3, column=1)
mezo2=Entry(ablak)
mezo2.grid(row=3, column=2)
gomb1=Button(ablak, text="számolás", command=ablak3)
gomb1.grid(row=4, column=2)

ablak.mainloop()
 