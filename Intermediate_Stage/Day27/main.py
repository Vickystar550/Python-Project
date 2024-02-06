import tkinter

# Creating Window:
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=600, height=600)
window.config(padx=20, pady=20)
# changing background color:
# screen = tkinter.Canvas(window, bg="white")
# screen.grid()


# Creating Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 20, "bold"))
# my_label.pack(side="top")
# my_label.place(x=250, y=250)
my_label.grid(column=1, row=1)


# Event Listener and Buttons:
def button_clicked():
    my_label.config(text=user_input.get())
    print("I got Clicked")


# Creating Buttons and Listening to events:
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack(side="top")
button.grid(column=2, row=2)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=3, row=1)


# Creating Entry:
user_input = tkinter.Entry(width=10)
# user_input.pack(side="bottom")
user_input.grid(column=4, row=3)

window.mainloop()
