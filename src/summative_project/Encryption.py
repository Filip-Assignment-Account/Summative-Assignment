import tkinter.messagebox
from typing import Any

import main
import math
import functools
from tkinter import *
from tkinter import ttk
import decimal

prime1 = 621869
prime2 = 655229

#TODO: display generated keys and messages to the user

"""Currently not working:
    -Decryption
    -Displaying messages/keys to user
"""

class Encryption:
    decimalcontext = decimal.Context(prec=decimal.MAX_PREC, Emax=decimal.MAX_EMAX)

    def generate_key(self, key: tuple | None) -> tuple[set[float | int], set[int]] | None:
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

    def tuple_key(self, key: str):
        """
        Turns str key into tuple key
        :param key: key in str
        :return: key in tuple
        """
        new_key = ''
        for letter in key:
            print("tuple_key: " + str(letter))
            if letter.isdigit() or letter == "." or letter == "+" or letter == "," or letter == "e":
                new_key = new_key + letter
        split_key = new_key.split(",")
        print("split key: " + str(split_key))
        print("key: " + str(key))
        if len(split_key) != 2:
            tkinter.messagebox.showerror("Invalid key", "Key must be in format (number, number) and cannot include both private and public keys at the same time")
            return None

        split_key[0] = float(split_key[0])
        split_key[1] = float(split_key[1])
        return split_key[0], split_key[1]


    def encrypt_text(self, msg: str, key: tuple) -> str | None:
        """
        Taking text and a public key as an input, encrypts text
        :param msg: Text to encrypt
        :param key: Encryption public key
        :return: Encrypted text
        """
        print("encrypt: key value: " + str(key))

        if not key:
            return

        public_key = key
        n, e = public_key

        encrypted_msg = ''
        try:
            for letter in msg:
                mangled_letter = pow(ord(letter), e) % n
                print("encrypt loop: " + str(letter))
                print("encrypt loop: " + str(e))
                print("encrypt loop: " + str(mangled_letter))
                while mangled_letter > 1114111: # chr has a limit of 1114111, this ensures that we're under that limit
                    mangled_letter = mangled_letter // 2
                    print("mangled_letter loop: " + str(mangled_letter))

                encrypted_msg = encrypted_msg + chr(int(mangled_letter))
                print("encrypt loop: " + encrypted_msg)
        except ValueError as e:
            tkinter.messagebox.showerror("Prime too big", "Inputted prime number was invalid or too big, error was: " + str(e))
        print(encrypted_msg)
        print("Encrypted")
        return encrypted_msg

    def decrypt_text(self, msg: str, key: tuple) -> str:
        """
        Same as encrypt_text, but the other way around
        :param msg: Encrypted text to decrypt
        :param key: Encryption private key
        :return: Unencrypted text
        """
        print("decrypt_text: key: " + str(key))
        private_key = key
        n, d = private_key

        decrypted_msg = ''
        try:
            for letter in msg:
                mangled_letter = pow(ord(letter), d) % n
                print("decrypt loop: " + str(letter))
                print("decrypt loop: " + str(d))
                print("decrypt loop: " + str(mangled_letter))

                while mangled_letter > 1114111:
                    mangled_letter = mangled_letter // 2
                    print("mangled_letter loop: " + str(mangled_letter))

                decrypted_msg = decrypted_msg + chr(int(mangled_letter))
                print("decrypt loop: " + decrypted_msg)
        except ValueError as e:
            tkinter.messagebox.showerror("Prime too big", "Inputted prime number was invalid or too big, error was: " + str(e))

        print(private_key)
        print("Decrypt")
        print(decrypted_msg)
        return decrypted_msg

    def is_prime(self, number: int) -> bool:
        """
        Checks if a number is a prime number
        :param number: Number to check
        :return: True if prime, false if not
        """
        print("isprime: Checking if "+ str(number) + " is prime")
        if number <= 1:
            return False
        for i in range(2, int(number**0.5) + 1):
            print("isprime: i is currently: "+ str(i))
            print(number % 1)
            if number % i == 0:
                return False
        return True

    def generate_keys_button(self, entry_prime1: object, entry_prime2: object) -> tuple[Any, Any] | None:
        """
        Handles the generate keys button click, defaulting to hardcoded prime numbers if no primes are present
        :param entry_prime1: User inputted prime number 1
        :param entry_prime2: User inputted prime number 1
        :return: Private/public key pair
        """
        prime_text1 = entry_prime1.get()
        prime_text2 = entry_prime2.get()
        print("button_encrypt: value of prime1_text: " + str(prime_text1))
        print("button_encrypt: value of prime2_text: " + str(prime_text2))
        try:
            print("Trying to run isprime")
            """if self.is_prime(int(prime1)) and self.is_prime(int(prime2)) and not is_decrypt:
                self.encrypt_text(entry_msg.get('1.0', 'end-1c'), (prime1, prime2))
            elif self.is_prime(int(prime1)) and is_prime(int(prime2)) and is_decrypt:
                self.Decrypt(entry_msg.get('1.0', 'end-1c'), (prime1, prime2))
            else:
                tkinter.messagebox.showerror("Error", "Value must be a prime integer")"""
            if prime_text1 == "" and prime_text2 == "":
                private_key, public_key = self.generate_key((prime1, prime2))
                return private_key, public_key
            elif self.is_prime(int(prime_text1)) and self.is_prime(int(prime_text2)):
                private_key, public_key = self.generate_key((prime_text1, prime_text2))
                return private_key, public_key
            else:
                tkinter.messagebox.showerror("Error", "Value must be a prime integer")
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error", "Value must be a prime integer")

    def __init__(self, window):
        def button_encrypt(is_decrypt: bool) -> None:
            key = key_input[0].get()
            if key == '' and not is_decrypt:
                self.encrypt_text(self.msg.get('1.0', 'end-1c'), self.generate_key(None)) # Gets text from beginning until the end of the text box
                return
            elif key == '' and is_decrypt:
                self.decrypt_text(self.msg.get('1.0', 'end-1c'), self.generate_key(None))
            elif is_decrypt:
                self.decrypt_text(self.msg.get('1.0', 'end-1c'), self.tuple_key(key))
            elif not is_decrypt:
                self.encrypt_text(self.msg.get('1.0', 'end-1c'), self.tuple_key(key))


        def validate_input(input): # to delete?
            if input.isdigit() or input == "":
                print("vaildation successful")
                return True
            else:
                tkinter.messagebox.showerror("Validation failed")
                return False

        window.add_title("Pick two prime numbers (optional): ", 1, 1)

        prime_inputs = window.add_entry(True, 100, 10, 2, 1, 2, False)
        entry_prime1 = prime_inputs[0]
        entry_prime2 = prime_inputs[1]

        key_input = window.add_entry(False, 100, 20, 4, 1, 1, False)
        window.add_title("Input private or public key pair here:", 1, 3)

        msg_label = ttk.Label(window, text="Enter a message to encrypt/decrypt")
        msg_label.grid(row=5, column=1, pady=(0,0))

        msg_container = ttk.Frame(window, height=10, width=100)
        msg_container.grid(row=6, column=1)
        self.msg = Text(msg_container, wrap='word', height=5, width=30)
        self.msg.grid(row=0, column=0)

        generate_keys_button = Button(window, text="Generate Keys", command=functools.partial(self.generate_keys_button, entry_prime1, entry_prime2))
        generate_keys_button.grid(row=2, column=3)

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
