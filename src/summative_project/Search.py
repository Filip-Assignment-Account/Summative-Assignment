from tkinter import *
from tkinter import ttk
import main
import Sorting
import functools


class Search:
    def __init__(self, window):
        sorting = Sorting.Sorting(None)


        def button_run(entry):
            sorted_arr = sorting.button_run(entry)
            print(sorted_arr)


        window.add_title("Search", 1, 1)

        self.entry = window.add_entry(True, 5, 1, 2, 1, 1, True)

        entry_button = ttk.Button(window, text="Run algorithm", command=functools.partial(button_run, self.entry))
        entry_button.grid(row=2, column=2)

        textbox_width = 8

        text_label = Label(window, text="Smallest:")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=1, width=textbox_width)
        self.text.grid(row=4, column=1)

        text2_label = Label(window, text="Largest:")
        text2_label.grid(row=5, column=1)
        self.text2 = Text(window, wrap='word', height=1, width=textbox_width)
        self.text2.grid(row=6, column=1)

        text3_label = Label(window, text="Median:")
        text3_label.grid(row=7, column=1)
        self.text3 = Text(window, wrap="word", height=1, width=textbox_width)
        self.text3.grid(row=8, column=1)

        text4_label = Label(window, text="1st and 3rd IQF")
        text4_label.grid(row=9, column=1)
        self.text4 = Text(window, wrap="word", height=1, width=textbox_width)
        self.text4.grid(row=10, column=1)
        
        self.text.config(state="disabled")


def init_window(main_window):
    window = main.Window("Search", 30, 100)
    window.add_back_button()
    window.parent = main_window
    search = Search(window)

