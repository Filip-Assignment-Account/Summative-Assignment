import main
import functools
from tkinter import ttk
from tkinter import *


class DynamicProgramming:
    def count(self, string):
        length = len(string)
        result = 0

        dp = [[False] * length for i in range(length)]

        for i in range(length):
            dp[i][i] = True

        for i in range(length - 1):
            if string[i] == string[i + 1]:
                dp[i][i + 1] = True
                print(result)
                result += 1

        for gap in range(2, length):
            for i in range(length - gap):
                j = i + gap
                if string[i] == string[j] and dp[i + 1][j - 1]:
                    print(result)
                    dp[i][j] = True
                    result += 1
        return result



    def __init__(self, window):
        def update_textbox(msg: int):
            self.text.config(state="normal")
            self.text.delete('1.0', END)
            self.text.insert(END, str(msg))
            self.text.config(state="disabled")

        def button_run():
            print("button_run: entry: " + str(self.entry[0].get()))
            result = self.count(self.entry[0].get())
            update_textbox(result)


        window.add_title("Palindrome count", 1, 1)

        self.entry = window.add_entry(False, 5, 1, 2, 1, 1, False)
        entry_button = ttk.Button(window, text="Run algorithm", command=functools.partial(button_run))
        entry_button.grid(row=2, column=2)

        text_label = Label(window, text="Output (scrollable):")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=5, width=30)
        self.text.grid(row=4, column=1)
        self.text.config(state="disabled")



def init_window(main_window):
    window = main.Window("Search", 30, 100)
    window.add_back_button()
    window.parent = main_window
    DynamicProgramming(window)