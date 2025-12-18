import tkinter.messagebox

import main
import math
import functools
from tkinter import *
from tkinter import ttk
prime1 = 52609494872530492621
prime2 = 52609494872530492621

class Encryption:
    def generate_key(self, key: tuple | None) -> tuple[set[float | int], set[int]] | None:# TODO: give user the keys instead of piping them directly into the algorithm
        """
        Generates a key pair using two prime numbers
        :param key: two prime numbers as a tuple
        :return: tuple containing the public/private key pair, contains another tuple holding mult_priv if private_key, or exponent if public_key, as well as primemult
        """
        print("generate_key: key value: " + str(key))
        if key:
            try:
                print("generate_key: key value received: " + str(key))
                self.prime1 = int(key[0])
                self.prime2 = int(key[1])
            except Exception as e:
                print("Exception in Generate key: " + str(e))
                tkinter.messagebox.showerror("Error", "Exception thrown: " + str(e))
                return
        else:
            self.prime1 = int(prime1)
            self.prime2 = int(prime2)

        print("generate_key: Primes set: " + str(self.prime1) + " and " + str(self.prime2))

        self.primemult = self.prime1 * self.prime2
        primemult_minusone = (self.prime1-1)*(self.prime2-1)
        exponent = 2

        while(exponent<primemult_minusone):
            if (math.gcd(exponent, primemult_minusone) == 1):
                break
            else:
                exponent += 1
                print("generate_key_loop: " + str(exponent))

        k = 2
        mult_priv = ((k*primemult_minusone)+1)/exponent
        private_key = {mult_priv, self.primemult}
        public_key = {exponent, self.primemult}

        print("generate_key: Key pair generated: " + str(private_key) + str(public_key))
        return private_key, public_key

    def encrypt_text(self, msg: str, key: tuple | None) -> str:
        print("encrypt: key value: " + str(key))
        keys = self.generate_key(key)
        print("encrypt: got key pair: " + str(keys))

        public_key = keys[1]
        n, e = public_key

        encrypted_msg = ''
        try:
            for letter in msg:
                mangled_letter = (ord(letter) ** e) % n
                print("encrypt loop: " + str(letter))
                print("encrypt loop: " + str(e))
                print("encrypt loop: " + str(mangled_letter))
                while mangled_letter > 1114111: # chr has a limit of 1114111, this ensures that we're under that limit
                    mangled_letter = mangled_letter // 2
                    print("mangled_letter loop: " + str(mangled_letter))

                encrypted_msg = encrypted_msg + chr(mangled_letter)
                print("encrypt loop: " + encrypted_msg)
        except ValueError as e:
            tkinter.messagebox.showerror("Prime too big", "Inputted prime number was invalid or too big, error was: " + str(e))
        print(encrypted_msg)
        print("Encrypted")
        return encrypted_msg

    def Decrypt(self, msg: str, key: tuple | None) -> str:
        keys = self.generate_key(key)

        private_key = keys[0]
        n, d = private_key

        decrypted_msg = ''
        try:
            for letter in msg:
                mangled_letter = (ord(letter) ** d) % n
                print("decrypt loop: " + str(letter))
                print("decrypt loop: " + str(d))
                print("decrypt loop: " + str(mangled_letter))

                while mangled_letter > 11141111:
                    mangled_letter = mangled_letter // 2
                    print("mangled_letter loop: " + str(mangled_letter))

                decrypted_msg = decrypted_msg + chr(mangled_letter)
                print("decrypt loop: " + decrypted_msg)
        except ValueError as e:
            tkinter.messagebox.showerror("Prime too big", "Inputted prime number was invalid or too big, error was: " + str(e))

        print(private_key)
        print("Decrypt")
        print(decrypted_msg)
        return decrypted_msg

    def __init__(self, window):
        def is_prime(number):
            print("isprime: Checking if "+ str(number) + " is prime")
            if number <= 1:
                return False
            for i in range(2, int(number**0.5) + 1):
                print("isprime: i is currently: "+ str(i))
                print(number % 1)
                if number % i == 0:
                    return False
            return True

        def button_encrypt(is_decrypt: bool) -> None:
            prime1_text = entry_prime1.get()
            prime2_text = entry_prime2.get()
            print("button_encrypt: value of prime1_text: " + str(prime1_text))
            print("button_encrypt: value of prime2_text: " + str(prime2_text))

            if prime1_text == '' and prime2_text == '' and not is_decrypt:
                self.encrypt_text(entry_msg.get('1.0', 'end-1c'), None) # Gets text from beginning until the end of the text box
                return
            elif prime1_text == '' and prime2_text == '' and is_decrypt:
                self.Decrypt(entry_msg.get('1.0', 'end-1c'), None)

            else:
                try:
                    print("Trying to run isprime")
                    if is_prime(int(prime1_text)) and is_prime(int(prime2_text)) and not is_decrypt:
                        self.encrypt_text(entry_msg.get('1.0', 'end-1c'), (prime1_text, prime2_text))
                    elif is_prime(int(prime1_text)) and is_prime(int(prime2_text)) and is_decrypt:
                        self.Decrypt(entry_msg.get('1.0', 'end-1c'), (prime1_text, prime2_text))
                    else:
                        tkinter.messagebox.showerror("Error", "Value must be a prime integer")
                except Exception as e:
                    print(e)
                    tkinter.messagebox.showerror("Error", "Value must be a prime integer")


        def validate_input(input):
            if input.isdigit() or input == "":
                print("vaildation successful")
                return True
            else:
                tkinter.messagebox.showerror("Validation failed")
                return False

        window.add_title("Pick two prime numbers (optional): ", 1, 1)

        """entry_container = ttk.Frame(window, height=10, width=100)
        entry_container.grid(row=2, column=1)

        vcmd = window.register(validate_input)

        entry_prime1 = Entry(entry_container, validate="key", validatecommand=(vcmd, "%P"))
        entry_prime1.grid(row=2, column=1, pady=10)
        entry_prime2 = Entry(entry_container, validate="key", validatecommand=(vcmd, "%P"))
        entry_prime2.grid(row=2, column=2, padx=10)"""

        prime_inputs = window.add_entry(True, 100, 10, 2, 1, 2, False)
        entry_prime1 = prime_inputs[0]
        entry_prime2 = prime_inputs[1]

        msg_label = ttk.Label(window, text="Enter a message to encrypt/decrypt")
        msg_label.grid(row=3, column=1, pady=(20,0))

        msg_container = ttk.Frame(window, height=10, width=100)
        msg_container.grid(row=4, column=1)

        entry_msg = Text(msg_container, width=30, height=2)
        entry_msg.grid(row=0, column=0, padx=(30,0))

        encrypt_button = Button(window, text="Encrypt text", command=functools.partial(button_encrypt, False))
        encrypt_button.grid(row=4, column=3)

        decrypt_button = Button(window, text="Decrypt text", command=functools.partial(button_encrypt, True))
        decrypt_button.grid(row=5, column=3)
        print(prime1)


def init_window(main_window: str):
    window = main.Window("Encryption", 40, 400)
    window.add_back_button()
    window.parent = main_window
    encryption = Encryption(window)
