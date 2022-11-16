import tkinter

def turn_red():
    root.configure(background='red')

def turn_blue():
    root.configure(background='blue')

root = tkinter.Tk()

red_button = tkinter.Button(root, text='Turn red', command=turn_red)
red_button.pack()

blue_button = tkinter.Button(root, text='Turn blue', command=turn_blue)
blue_button.pack()

root.mainloop()