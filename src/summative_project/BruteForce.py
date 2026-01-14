import main
from tkinter import *
from tkinter import ttk

class BruteForce:
    def merge(self, array, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        #Split array into left and right sections
        for a in range(n1):
            L[a] = array[left + a]
        for b in range(n2):
            R[b] = array[mid + 1 + b]

        a = 0
        b = 0
        k = left

        while a < n1 and b < n2:
            if L[a] <= R[b]:
                array[k] = L[a]
                a += 1
            else:
                array[k] = R[b]
                b += 1
            k += 1

        #any residual elements get handled here
        while a < n1:
            array[k] = L[a]
            a += 1
            k += 1

        while b < n2:
            array[k] = R[b]
            b += 1
            k += 1

    def merge_sort(self, array, left, right):
        if left < right:
            mid = (left + right) // 2
            # Using recursion, merge the split arrays together
            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid + 1, right)
            self.merge(array, left, mid, right)
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
        Handles integer validation and runs the function
        :param entry:
        :return:
        """
        entry_input = entry[0].get()
        print("button run: " + entry_input)
        entry_array = []
        entry_number = ""
        for i in entry_input:
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
        sorted_array = self.merge_sort(entry_array, 0, len(entry_array) - 1)
        self.update_textbox(sorted_array)




    def __init__(self, window):
        window.add_title("Divide and conquer", 1, 1)
        entry = window.add_entry(True, 5, 1, 2, 1, 1, True)
        entry_button = ttk.Button(window, text="Run algorithm", command=main.functools.partial(self.button_run, entry))
        entry_button.grid(row=2, column=2)

        text_label = Label(window, text="Output (scrollable):")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=5, width=30)
        self.text.grid(row=4, column=1)
        self.text.config(state="disabled")
        

def init_window(main_window):
    window = main.Window("Brute Force", 30, 100)
    window.add_back_button()
    window.parent = main_window
    bruteforce = BruteForce(window)