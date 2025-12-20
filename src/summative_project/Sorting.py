import main
from tkinter import ttk
from tkinter import *


class Sorting:
    def selection_sort(self, array):
        print("running selection sort")
        arr_len = len(array)
        for i in range(arr_len - 1):
            minimum_index = i

            for j in range(i + i, arr_len):
                if array[j] < array[minimum_index]:
                    minimum_index = j

            array[i], array[minimum_index] = array[minimum_index], array[i]

    def bubble_sort(self, array):
        print("running bubble sort")
        arr_len = len(array)
        for i in range(arr_len):
            swapped = False
            for j in range(0, arr_len-i-1):
                print("Bubble sort: " + str(j))
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            if not swapped:
                break

    def button_run(self, entry):
        entry_input = entry[0].get()
        print("button run: " + entry_input)
        entry_array = []
        entry_number = ""
        for i in entry_input:
            if i != " ":
                entry_number = entry_number + i
            if i == " ":
                print("button_run: detected space, entry_number: " + str(entry_number))
                entry_array.append(entry_number)
                print("button_run: entry_array: " + str(entry_array))
                entry_number = ""
        if entry_number != "":
            entry_array.append(entry_number) # If last number is not added to the final array
            print("button_run: final number appended")

        print("button_run: final entry_array: " + str(entry_array))
        print("button_run: got dropdown var: " + str(self.opt.get()))

        if self.opt.get() == "Selection Sort":
            print("button_run: got selection sort")
            self.selection_sort(entry_array)
        if self.opt.get() == "Bubble Sort":
            print("button_run: got bubble sort")
            self.bubble_sort(entry_array)

    def __init__(self, window):
        window.add_title("Sorting algorithm", 1, 1)
        entry = window.add_entry(True, 5, 1, 2, 1, 1, True)
        entry_button = ttk.Button(window, text="Run algorithm", command=main.functools.partial(self.button_run, entry))
        entry_button.grid(row=2, column=2)

        self.options = ["Selection Sort", "Bubble Sort"]
        self.opt = StringVar(window)
        self.dropdown = ttk.OptionMenu(window, self.opt, self.options[0],*self.options)
        self.dropdown.grid(row=3, column=2)

        text_label = Label(window, text="Output:")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=2, width=30)
        self.text.grid(row=4, column=1)
        self.text.config(state="disabled")
        

def init_window(main_window):
    window = main.Window("Sorting", 30, 100)
    window.add_back_button()
    window.parent = main_window
    sorting = Sorting(window)
