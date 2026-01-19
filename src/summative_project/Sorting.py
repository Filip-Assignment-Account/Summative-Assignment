import main
from tkinter import ttk
from tkinter import *


class Sorting:
    def selection_sort(self, array: list) -> list:
        """
        Given a list input, outputs a sorted list using the selection sort algorithm
        :param array: List to sort
        :return: Sorted list
        """
        print("running selection sort")
        arr_len = len(array)
        for i in range(arr_len):
            minimum_index = i
            for j in range(i + 1, arr_len):
                if array[j] < array[minimum_index]:
                    minimum_index = j

            array[i], array[minimum_index] = array[minimum_index], array[i]
            #print("selection sort: " + str(array))
        print("final array: " + str(array))
        return array

    def bubble_sort(self, array):
        """
            Given a list input, outputs a sorted list using the bubble sort algorithm
            :param array: List to sort
            :return: Sorted list
        """
        print("running bubble sort")
        arr_len = len(array)
        for i in range(arr_len):
            swapped = False
            for j in range(0, arr_len-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    #print("Bubble sort: " + str(array))
                    swapped = True
            if not swapped:
                print("final array: " + str(array))
                return array

    def update_textbox(self, msg: str) -> None:
        """
        Updates output textbox with arbitrary text
        :param msg: Text to put in the textbox
        :return: None
        """
        self.text.config(state="normal") # Text won't be written unless textbox is enabled for a short period of time
        self.text.delete('1.0', END)
        self.text.insert(END, str(msg))
        self.text.config(state="disabled")

    def button_run(self, entry: list) -> None:
        """
        Handles which algorithm to run and ensures that each index is an integer when the user clicks the button
        :param entry:
        :return:
        """
        print("button run: " + str(entry))
        entry_array = []
        entry_number = ""
        for i in entry:
            if i != " ":
                entry_number = entry_number + i
            if i == " ": # Separate each index by a space
                print("button_run: detected space, entry_number: " + str(entry_number))
                entry_array.append(int(entry_number))
                print("button_run: entry_array: " + str(entry_array))
                entry_number = ""
        if entry_number != "":
            entry_array.append(int(entry_number)) # If last number is not added to the final array
            print("button_run: final number appended")

        print("button_run: final entry_array: " + str(entry_array))
        try:
            print("button_run: got dropdown var: " + str(self.opt.get()))

            if self.opt.get() == "Selection Sort":
                print("button_run: got selection sort")
                sorted_array = self.selection_sort(entry_array)
                self.update_textbox(sorted_array)
            if self.opt.get() == "Bubble Sort":
                print("button_run: got bubble sort")
                sorted_array = self.bubble_sort(entry_array)
                self.update_textbox(sorted_array)
        except AttributeError:
            self.selection_sort(entry_array) # for if being run outside this file

    def __init__(self, window):
        if not window:# If other files need functions from here we don't want to create a window
            print("Sorting: called from somewhere else, skipping window setup")
            return
        window.add_title("Sorting algorithm", 1, 1)
        entry = window.add_entry(True, 5, 1, 2, 1, 1, True)
        entry_button = ttk.Button(window, text="Run algorithm", command=main.functools.partial(self.button_run, entry))
        entry_button.grid(row=2, column=2)

        self.options = ["Selection Sort", "Bubble Sort"]
        self.opt = StringVar(window)
        self.dropdown = ttk.OptionMenu(window, self.opt, self.options[0],*self.options)
        self.dropdown.grid(row=3, column=2)

        text_label = Label(window, text="Output (scrollable):")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=5, width=30)
        self.text.grid(row=4, column=1)
        self.text.config(state="disabled")
        

def init_window(main_window):
    window = main.Window("Sorting", 30, 100)
    window.add_back_button()
    window.parent = main_window
    sorting = Sorting(window)
