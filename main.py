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
        print()


class Window(Tk):
    def __init__(self, title, h, w, back):
        self.parent = None
        def cleanly_exit():
            exit(0)
        def go_Back():
            if self.parent:
                self.parent.deiconify()
            self.destroy()

        Tk.__init__(self)
        self.title(title)
        container = ttk.Frame(self, height=h, width=w)
        container.grid(row=0, column=1)
        self.protocol('WM_DELETE_WINDOW', cleanly_exit)
        global active_window
        active_window = self

        if back == True:
            exit_Button = ttk.Button(container, text="Back", command=go_Back)
            exit_Button.grid(row=0, column=0)


if __name__ == "__main__":  # Need this here for the class to run
    window = Window("Algorithm Selection", 100, 100, False)
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
        if i > button_Range/2:
            button_Flag = 1
            if counter == i:
                counter = 0
        else:
            button_Flag = 0
        button = ttk.Button(window, text=str(button_Names[i]), # Planned: make graphical buttons using classes
            command=functools.partial(button_click, button_Names[i], main_window))
        button.grid(column=counter, row=button_Flag)

    window.mainloop()
