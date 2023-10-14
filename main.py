import tkinter

# window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=350, height=350)


# def

def calculate():
    weight = float(entry1.get())
    height = float(entry2.get()) / 100
    result = weight / (height * height)
    if result < 18.5:
        label3.config(text='UNDERWEIGHT', font=("Arrival", 10, 'bold'))
    elif 18.5 < result <= 24.9:
        label3.config(text='NORMAL', font=("Arrival", 10, 'bold'))
    elif 24.9 < result <= 29.9:
        label3.config(text='OVERWEIGHT', font=("Arrival", 10, 'bold'))
    elif 29.9 < result <= 34.9:
        label3.config(text='OBESE', font=("Arrival", 10, 'bold'))
    elif result >= 35:
        label3.config(text='EXTREMLY OBESE', font=("Arrival", 10, 'bold'))


# label 1
label1 = tkinter.Label(text="Enter Your Weight(kg)")
label1.place(x=110, y=70)

# entry 1
entry1 = tkinter.Entry()
entry1.place(x=110, y=100)

# label 2
label2 = tkinter.Label(text="Enter Your Height(cm)")
label2.place(x=110, y=130)

# entry 2
entry2 = tkinter.Entry()
entry2.place(x=110, y=160)

# button

button = tkinter.Button(text='Calculate', command=calculate)
button.place(x=135, y=190)

# label 3
label3 = tkinter.Label(text=" ")
label3.place(x=135, y=250)

window.mainloop()
