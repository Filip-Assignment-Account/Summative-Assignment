import main


class Sorting:
    def selection_sort(self):


    def __init__(self, window):
        window.add_title("Sorting algorithm", 1, 1)


def init_window(main_window):
    window = main.Window("Sorting", 30, 100)
    window.add_back_button()
    window.parent = main_window
    sorting = Sorting(window)
