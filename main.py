import tkinter.messagebox
from tkinter import *
from tkinter import ttk
import functools

import Encryption

active_window = None
main_window = None


def button_click(name: str, parent: str) -> None:
    """
    Handles button clicks and runs corresponding window functions from other windows
    :param name: Name of the window
    :param parent: Parent of the window (usually this one, main.py)
    :return: None
    """
    window.withdraw()
    match name:
        case 'Encryption':
            Encryption.init_encryption_window(parent)
        case 'Fibonacci Numbers':
            print("fib")
        case _:
            tkinter.messagebox.showerror("Error", "Missing page for \"" + str(name) + "\" button")
            window.deiconify()


class Window(Tk):
    def go_back(self) -> None:
        """
        Destroys current window and goes back to previous window
        :return: None.
        """
        if self.parent:
            self.parent.deiconify()
        self.destroy()

    def add_back_button(self) -> None:
        """
        Adds back button to the top left of a window.
        :return: None.
        """
        exit_button = ttk.Button(self.container, text="Back", command=self.go_back)
        exit_button.place(x=0, y=0)

    def add_title(self, text: str, gridx: int, gridy: int) -> None:
        """
        Adds title to a window.
        Args:

        :param text: Text to add as title.
        :param gridx: Same as column=
        :param gridy: Same as row=
        :return: None.
        """
        title_container = ttk.Frame(self, height=1, width=50)
        title_container.grid(row=gridy, column=gridx)
        title_label = ttk.Label(title_container, text=text)
        title_label.config(font=("Arial", 15))
        title_label.grid(row=0, column=0, padx=(40, 0))

    def __init__(self, title: str, h: int, w: int) -> None:
        """
        Creates a window with a title, height and weight. Automatically creates a container inside the window and handles exiting behaviour.
        :param title: Title of the window
        :param h: Height of the container within the window
        :param w: Width of the container in the window
        """
        self.parent = None

        def cleanly_exit() -> None:
            """
            Exits application when no windows are open so that the application doesn't remain dormant in the background
            :return: None
            """
            exit(0)

        Tk.__init__(self)
        self.title(title)
        self.container = ttk.Frame(self, height=h, width=w)
        self.container.grid(row=0, column=1)
        self.protocol('WM_DELETE_WINDOW', cleanly_exit)
        global active_window
        active_window = self


class Button(Tk):
    def __init__(self, window: Window, function: any) -> None:
        #super().__init__() # May be needed, find out later
        self.Button = ttk.Button(window, command=functools.partial(function, button_Names[i], window))
    def Grid_button(self, column, row):
        self.Button.grid(column=column, row=row)


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
