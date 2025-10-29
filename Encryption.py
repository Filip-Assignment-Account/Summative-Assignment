import main

prime1 = 857501480975746940207863753291
prime2 = 884671140447678060778666300543

def init_encryption_window(main_window):
    window = main.Window("Encryption", 300, 300, True)
    window.parent = main_window
    print(prime1)