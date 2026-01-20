from __future__ import annotations
import sys
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import main


class Fibonacci:
    def find_fibonacci(self, n: int) -> int:
        """
        An iterative approach to find fibonacci numbers with O(n) time complexity
        :param n: Which term along the sequence to look for
        :return: The resulting fibonacci number
        """
        if n <= 1:
            return n

        current_num = 0
        previous_num1 = 1
        previous_num2 = 0

        for i in range(2, n + 1):
            current_num = previous_num1 + previous_num2
            previous_num2 = previous_num1
            previous_num1 = current_num

        
        return current_num

    def button_run(self, entry: list) -> None:
        """
        Handles button click
        :param entry: Which number to get, in list format as this object also accommodates multiple entries in one object
        :return: None
        """
        if int(entry[0].get()) > 9999:
            yes = messagebox.askyesno("Are you sure?", "This is a large number and may not fit on screen or may cause a freeze, do you want to continue?")
            if not yes:
                return

        self.label.grid(row=2, column=1, padx= (100, 0))
        self.window.update()
        num = self.find_fibonacci(int(entry[0].get()))

        print(num)
        self.label.grid_forget()
        messagebox.showinfo("Fibonacci", f"The fibonacci number at position {entry[0].get()} is: {num}")

    def __init__(self, window):
        sys.set_int_max_str_digits(0) # allows for ludicrous numbers > 4300 digits
        window.add_title("Enter the nth fibonacci number to calculate", 1, 0)
        entry = window.add_entry(True, 5, 5, 1, 1, 1, False)
        self.label = Label(window, text="Loading...", font=("Arial", 16), bg="lightblue")
        self.window = window

        entry_button = ttk.Button(window, text="Run algorithm", command=main.functools.partial(self.button_run, entry))
        entry_button.grid(row=1, column=2)
        

def init_window(main_window):
    window = main.Window("Fibonacci", 200, 300)
    window.add_back_button()
    window.parent = main_window
    fibonacci = Fibonacci(window)
