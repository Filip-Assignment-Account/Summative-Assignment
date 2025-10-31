import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import functools

import Encryption

active_window = None
main_window = None


def button_click(name, parent):
    window.withdraw()
    match name:
        case 'Encryption':
            Encryption.init_encryption_window(parent)
        case _:
            tkinter.messagebox.showerror("Error", "Missing page for \"" + str(name) + "\" button")
            window.deiconify()


class Button(Tk):
    def __init__(self):
        #super().__init__() # May be needed, find out later
        print()


class Window(Tk):
    def go_back(self):
        if self.parent:
            self.parent.deiconify()
        self.destroy()

    def Add_Back_Button(self):
        exit_button = ttk.Button(self.container, text="Back", command=self.go_back)
        exit_button.grid(row=0, column=0)

    def __init__(self, title, h, w):
        self.parent = None

        def cleanly_exit():
            exit(0)

        Tk.__init__(self)
        self.title(title)
        self.container = ttk.Frame(self, height=h, width=w)
        self.container.grid(row=0, column=1)
        self.protocol('WM_DELETE_WINDOW', cleanly_exit)
        global active_window
        active_window = self


if __name__ == "__main__":  # Need this here for the class to run
    window = Window("Algorithm Selection", 100, 100)
    main_window = window
    button_Names = ["Encryption", "Fibonacci Numbers", "Sorting", "Brute Force",
                    "Randomised", "Recursion", "Search", "Dynamic Programming",
                    "Behavioral Design Pattern", "Creational Design Pattern",
                    "Structural Design Pattern"]
    button_Range = len(button_Names)
    counter = -1
    button_Flag = 0
    for i in range(button_Range):
        counter = counter + 1
        if i > button_Range / 2:
            button_Flag = 1
            if counter == i:
                counter = 0
        else:
            button_Flag = 0
        button = ttk.Button(window, text=str(button_Names[i]),  # Planned: make graphical buttons using classes
                            command=functools.partial(button_click, button_Names[i], main_window))
        button.grid(column=counter, row=button_Flag)

    window.mainloop()
