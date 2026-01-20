import main
import sys
from tkinter import *
from tkinter import ttk


class Factorial:
    def factorial(self, num):
        calced_num = 1

        for i in range(num):
            if i == 0:
                i = 1
            calced_num = i * calced_num
            print("calced_num = " + str(calced_num))
        print(calced_num)
        return calced_num


    def __init__(self, window):
        sys.set_int_max_str_digits(0)
        def update_textbox(msg: str) -> None: # Consider making this a class in main
            """
            Updates output textbox with arbitrary text
            :param msg: Text to put in the textbox
            :return: None
            """
            self.text.config(state="normal")  # Text won't be written unless textbox is enabled for a short period of time
            self.text.delete("1.0", END)
            self.text.insert(END, str(msg))
            self.text.config(state="disabled")

        def button_run():
            factorial = self.factorial(int(self.entry[0].get()))
            update_textbox(str(factorial))


        self.entry = window.add_entry(True, 5, 1, 2, 1, 1, True)
        window.add_title("Factorial", 1, 1)
        text_label = Label(window, text="Output (scrollable):")
        text_label.grid(row=3, column=1)
        entry_button = ttk.Button(window, text="Run algorithm", command=button_run)
        entry_button.grid(row=2, column=2)

        self.text = Text(window, wrap='word', height=5, width=30)
        self.text.grid(row=4, column=1)
        self.text.config(state="disabled")



def init_window(main_window):
    window = main.Window("Factorial", 30, 100)
    window.add_back_button()
    window.parent = main_window
    factorial = Factorial(window)