from tkinter import *
from tkinter import ttk
import main
import Sorting
import functools


class Search:
    def __init__(self, window):
        sorting = Sorting.Sorting(None)

        def update_textbox(textbox: int, value: int | str) -> None:
            """
            Updates a textbox noted by the textbox parameter
            :param textbox: Textbox to update
            :param value: Text to update the textbox with
            :return:
            """
            self.textboxes[textbox].config(state="normal")
            self.textboxes[textbox].delete("1.0", END)
            self.textboxes[textbox].insert(END, str(value))
            self.textboxes[textbox].config(state="disabled")

        def split_list(array: list) -> tuple:
            """
            Splits array into two halves
            :param array: Array to split
            :return: First half of array, second half of array
            """
            half = len(array)//2
            return array[:half], array[half:]


        def fill_textboxes(array: list) -> None:
            """
            Fills text boxes with corresponding data
            :param array: array
            :return: None
            """
            update_textbox(0, array[0])
            length = len(array)
            update_textbox(1, array[length-1])
            update_textbox(2, array[length//2])
            first_half, last_half = split_list(array)
            last_half_length = len(last_half)
            update_textbox(3, str(array[length//4]) + " " + str(last_half[last_half_length//2]))


        def button_run(entry: list) -> None:
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

