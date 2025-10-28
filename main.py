from tkinter import *
from tkinter import ttk


class Window(Tk):
    def __init__(self, title):
        Tk.__init__(self)
        self.title(title)
        container = ttk.Frame(self, height=300, width=300)
        container.grid(row=0, column=0)
        self.mainloop()


if __name__ == "__main__": # Need this here for the class to run
    window = Window("egg")
    Button_names = {"Encryption", "Fibonacci Numbers", "Sorting", "Brute Force",
                    "Randomised", "Recursion", "Search", "Dynamic Programming",
                    "Behavioral Design Pattern", "Creational Design Pattern",
                    "Structural Design Pattern"}

    window.mainloop()





