import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# components
my_label = tkinter.Label(text="name: ", font=("Arial", 20, "bold"))
my_label["text"] = 'Next Text'
# my_label.pack(side='left')
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

def button_click():
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Me", command=button_click)
# button.pack(side="left")
# button.place(x=100, y=30)
button.grid(column=0, row=1)

input = tkinter.Entry(width=20)
# input.pack(side="left")
input.grid(column=0, row=2)

window.mainloop()
