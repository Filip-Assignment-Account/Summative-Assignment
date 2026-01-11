import main

class BruteForce:
    def merge(self, array, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        #Split array into left and right sections
        for i in range(n1):
            L[i] = array[left + i]
        for j in range(n2):
            R[j] = array[mid + 1 + j]

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
            i += 1
            k += 1

        while b < n2:
            array[k] = R[b]
            j += 1
            k += 1

    def merge_sort(self, array, left, right):
        if left < right:
            mid = (left + right) // 2
            # Using recursion, merge the split arrays together
            self.merge_sort(array, left, mid)
            self.merge_sort(array, mid + 1, right)
            self.merge(array, left, mid, right)




    def __init__(self):
        

def init_window(main_window):
    window = main.Window("Brute Force", 30, 100)
    window.add_back_button()
    window.parent = main_window
    bruteforce = BruteForce(window)