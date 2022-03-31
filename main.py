from tkinter import *
window = Tk()
window.title("Mile to km coverter")

window.config(padx=10, pady=10)

def calculate():
    number = input.get()
    number = int(number) * 1.609344
    number = int(number)
    number = str(number)
    label_2.config(text=number)

input = Entry(width=10)
input.grid(column=1,row=0)

label_1 = Label(text='Is equal to:')
label_1.grid(column=0 , row=1)

label_2 = Label(text='0')
label_2.grid(column=1 , row=1)

label_3 = Label(text='Km')
label_3.grid(column=2 , row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)





















window.mainloop()