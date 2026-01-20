from tkinter import *
from tkinter import ttk
import main
import Sorting
import functools


class Search:
    def __init__(self, window):
        sorting = Sorting.Sorting(None)

        def update_textbox(textbox: int, value: int):
            self.textboxes[textbox].config(state="normal")
            self.textboxes[textbox].delete("1.0", END)
            self.textboxes[textbox].insert(END, str(value))
            self.textboxes[textbox].config(state="disabled")


        def fill_textboxes(array):
            update_textbox(0, array[0])
            length = len(array)
            update_textbox(1, array[length-1])
            update_textbox(2, array[length//2])


        def button_run(entry):
            validated_arr = sorting.validate_spaces(entry[0].get())
            if not validated_arr:
                return
            sorted_arr = sorting.selection_sort(validated_arr)
            fill_textboxes(sorted_arr)


        window.add_title("Search", 1, 1)

        self.entry = window.add_entry(True, 5, 1, 2, 1, 1, True)

        entry_button = ttk.Button(window, text="Run algorithm", command=functools.partial(button_run, self.entry))
        entry_button.grid(row=2, column=2)

        textbox_width = 8

        text = ["Smallest:", "Largest:", "Median:", "1st and 3rd IQF"]
        self.textboxes = []
        text_labels = []
        count = 0

        for i in text:
            print(i)
            text_label = Label(window, text=i)
            text_labels.append(text_label)
            textbox = Text(window, wrap='word', height=1, width=textbox_width)
            self.textboxes.append(textbox)
        for i in self.textboxes:
            i.grid(row=4+count, column=1)
            count += 2

        count = 0

        for i in text_labels:
            i.grid(row=3+count, column=1)
            count += 2



def init_window(main_window):
    window = main.Window("Search", 30, 100)
    window.add_back_button()
    window.parent = main_window
    search = Search(window)

