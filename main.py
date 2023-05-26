import random
from tkinter import StringVar, Label, Tk, Entry


window = Tk()
window.geometry("500x500")
window.title("Monty Hall Simulator")

same_choice = StringVar()
switched_choice = StringVar

same_choice.set(0)
switched_choice.set(0)

no_sample = Entry()

Label1 = Label(window, text='Same Choice').place(x=80, y=8)
label2 = Label(window, text='Switch Choice').place(x=80, y=40)
label3 = Label(window, textvariable=same_choice, font=(15)).place(x=180, y=40)
no_sample.place(x=100, y=70)


window.mainloop()
