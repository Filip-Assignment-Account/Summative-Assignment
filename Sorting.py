import main


class Sorting:
    def selection_sort(self, array):
        arr_len = len(array)
        for i in range(arr_len - 1):
            minimum_index = i

            for j in range(i + i, arr_len):
                if array[j] < array[minimum_index]:
                    minimum_index = j

            array[i], array[minimum_index] = array[minimum_index], array[i]
    def bubble_sort(self, array):
        arr_len = len(array)
        for i in range(arr_len):
            swapped = False
            for j in range(0, arr_len-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            if not swapped:
                break


    def __init__(self, window):
        window.add_title("Sorting algorithm", 1, 1)


def init_window(main_window):
    window = main.Window("Sorting", 30, 100)
    window.add_back_button()
    window.parent = main_window
    sorting = Sorting(window)
