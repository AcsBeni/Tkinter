
from tkinter import *
from tkinter import messagebox

root = Tk()

# Képernyő beállítások
root.title("Téglalap oldalai")
root.geometry("400x200")

# Feliratok
label1 = Label(root, text="Adja meg az a oldalt:")
label1.pack()

# Téglalap oldalainak bekérése
a = Entry(root)
a.pack()

label2 = Label(root, text="Adja meg a b oldalt:")
label2.pack()

b = Entry(root)
b.pack()

# Gomb
def calculate():
    a_value = int(a.get())
    b_value = int(b.get())
    area = a_value * b_value
    perimeter = 2 * (a_value + b_value)
    result = "Terület: " + str(area) + "\n" + "Kerület: " + str(perimeter)
    messagebox.showinfo("Eredmény", result)

button = Button(root, text="Számol", command=calculate)
button.pack()

root.mainloop()