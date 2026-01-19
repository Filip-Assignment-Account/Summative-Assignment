from tkinter import *
from tkinter import ttk
import main
import Sorting


class Search:
    def __init__(self, window):
        def sort_array(array):
            sorting = Sorting(self)
            sorted_array = sorting.selection_sort()
            return sorted_array


        def button_run():
            sort_array


        window.add_title("Search", 1, 1)
        entry_button = ttk.Button(window, text="Run algorithm", command=button_run)
        entry_button.grid(row=2, column=2)

        text_label = Label(window, text="Smallest:")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=1, width=5)
        self.text.grid(row=4, column=1)

        text2_label = Label(window, text="Largest:")
        text2_label.grid(row=5, column=1)
        self.text2 = Text(window, wrap='word', height=1, width=5)
        self.text2.grid(row=6, column=1)

        text3_label = Label(window, text="Median:")
        text3_label.grid(row=7, column=1)
        self.text3 = Text(window, wrap="word", height=1, width=5)
        self.text3.grid(row=8, column=1)

        text4_label = Label(window, text="1st and 3rd IQF")
        text4_label.grid(row=9, column=1)
        self.text4 = Text(window, wrap="word", height=1, width=5)
        self.text4.grid(row=10, column=1)
        
        self.text.config(state="disabled")


def init_window(main_window):
    window = main.Window("Search", 30, 100)
    window.add_back_button()
    window.parent = main_window
    search = Search(window)

