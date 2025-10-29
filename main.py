from tkinter import *
from tkinter import ttk


def is_Even(number):
    if number % 2 == 0:
        return 1
    else:
        return 0


class Window(Tk):
    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)
        container = ttk.Frame(self, height=3, width=3)
        container.grid(row=0, column=0)


if __name__ == "__main__":  # Need this here for the class to run
    window = Window("egg")
    button_Names = ["Encryption", "Fibonacci Numbers", "Sorting", "Brute Force",
                    "Randomised", "Recursion", "Search", "Dynamic Programming",
                    "Behavioral Design Pattern", "Creational Design Pattern",
                    "Structural Design Pattern"]
    for i in range(len(button_Names)):
        button = ttk.Button(window, text=str(button_Names[i]))
        button.grid(column=i, row=is_Even(i))

    window.mainloop()
