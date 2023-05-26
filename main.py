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


def simulate(event):
    same_choice_result = 0
    switched_choice_result = 0
    samples = int(no_sample.get())
    doors = ['gold', 'goat', 'bed']

    for i in range(samples):
        simulated_doors = doors.copy()
        random.shuffle(simulated_doors)
        first_choice = random.choice(simulated_doors)
        simulated_doors.remove(first_choice)

        opened_door = (
            simulated_doors[0] if simulated_doors[0] != 'gold' else simulated_doors[1])

        simulated_doors.remove(opened_door)
        switched_second_choice = simulated_doors[0]

        if first_choice == 'gold':
            same_choice_result += 1
            same_choice.set(same_choice_result)

        elif switched_second_choice == 'gold':
            switched_choice_result += 1
            switched_choice.set(switched_choice_result)

        else:
            print("That's will never happend.")


window.mainloop()
