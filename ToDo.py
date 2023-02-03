from tkinter import *

# All use of TKinter starts with this command
root = Tk()

# TKinter is always a two step process: "define" and "put on screen" 
# define it:   Creating a Label Widget
myLabel1 = Label(root, text="Mark's To Do List")
#myLabel2 = Label(root, text="My Name is Mark Brown")
# Another way to attach dot functions
myLabel3 = Label(root, text="Time To Get Tasks Done!")
# put on screen:  Shove it on screen anywhere use:
# myLabel1.pack()

myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)
myLabel3.grid(row=3, column=3)

# Entry widget
e = Entry(root, width=50,bg="#e0e0eb", fg="blue", borderwidth=5 )
e.grid(row=5, column=4)
e.insert(0, "Enter Your To Do")

 # text=e.get()

def myClick():
    HelloToDo = "Your new to To Do:  " + e.get()
    myLabel = Label(root, text=HelloToDo)
    myLabel.grid(row=6, column=4)

# 
myButton = Button(root, text="New To Do",  padx=25, pady=5,command=myClick, fg="#640032", background="blue", bg="#BdB768", borderwidth=5)
myButton.grid(row=4, column=4)

root.mainloop()

# TKinter uses a grid system of rows and columns
