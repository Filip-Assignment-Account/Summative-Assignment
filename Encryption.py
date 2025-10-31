import main

prime1 = 857501480975746940207863753291
prime2 = 884671140447678060778666300543

class Encryption:
    def Decrypt(self):
        print("Decrypt")
    def Encrypt(self):
        print("Encrypted")

    def __init__(self):
        print("placeholder")


def init_encryption_window(main_window):
    window = main.Window("Encryption", 300, 300)
    window.Add_Back_Button()
    window.parent = main_window
    print(prime1)