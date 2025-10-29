from tkinter import *
from tkinter import ttk
import functools

import Encryption

def button_Click(name):
    window.withdraw()
    Encryption.init_encryption_window()

def is_Even(number):
    if number % 2 == 0:
        return 1
    else:
        return 0


class Button(Tk):
    def __init__(self):
        print()


class Window(Tk):
    def __init__(self, title, h, w):
        def cleanly_exit():
            exit(0)
        Tk.__init__(self)
        self.title(title)
        container = ttk.Frame(self, height=h, width=w)
        container.grid(row=0, column=0)
        self.protocol('WM_DELETE_WINDOW', cleanly_exit)


if __name__ == "__main__":  # Need this here for the class to run
    window = Window("Algorithm Selection", 100, 100)
    button_Names = ["Encryption", "Fibonacci Numbers", "Sorting", "Brute Force",
                    "Randomised", "Recursion", "Search", "Dynamic Programming",
                    "Behavioral Design Pattern", "Creational Design Pattern",
                    "Structural Design Pattern"]
    button_Range = len(button_Names)
    counter = -1
    button_Flag = 0
    for i in range(button_Range):
        counter = counter + 1
        print("i = " + str(i))
        print("counter = " + str(counter))
        if i > button_Range/2:
            button_Flag = 1
            if counter == i:
                counter = 0
        else:
            button_Flag = 0
        button = ttk.Button(window, text=str(button_Names[i]), # Planned: make graphical buttons using classes
            command=functools.partial(button_Click, button_Names[i]))
        button.grid(column=counter, row=button_Flag)

    window.mainloop()
