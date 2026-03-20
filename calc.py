from tkinter import *
def add():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))
root=Tk()
root.title("Calculator")
root.geometry("400x400")

label1 = Label(root, text="Number 1:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

label2 = Label(root, text="Number 2:")
label2.pack()
entry2 = Entry(root)
entry2.pack()

button_add = Button(root, text="Add", command=add)
button_add.pack()

label_result = Label(root, text="Result: ")
label_result.pack()

root.mainloop()
