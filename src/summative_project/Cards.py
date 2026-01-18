from tkinter import *
from tkinter import ttk
import main
import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
suits = ["Diamonds", "Clubs", "Spades", "Hearts"]

class Card:
    def get_card(self) -> list:
        """
        Gets current card
        :return: Card type and suit
        """
        return [self.card, self.suit]
    def __init__(self, card, suit):
        if card in cards:
            self.card = card
        if suit in suits:
            self.suit = suit

class Cards:
    def get_full_deck(self) -> list: #Consider moving constructor to a separate function to avoid constantly constructing card objects
        """
        Constructs cards and appends them to a deck list for each suit and card combination available
        :return: full deck in a list
        """
        deck = []
        for i in cards:
            for j in suits:
                card = Card(i, j)
                deck.append(card)
        for i in range(len(deck)):
            print(deck[i].get_card())
        return deck

    def shuffle_cards(self) -> list:
        """
        Shuffles deck and returns list of cards in a random order
        :return: shuffled deck
        """
        deck = self.get_full_deck()
        random.shuffle(deck)
        return deck

    def __init__(self, window):
        def update_textbox(msg: str) -> None: # Consider making this a class in main
            """
            Updates output textbox with arbitrary text
            :param msg: Text to put in the textbox
            :return: None
            """
            self.text.config(state="normal")  # Text won't be written unless textbox is enabled for a short period of time
            self.text.delete("1.0", END)
            self.text.insert(END, str(msg))
            self.text.config(state="disabled")

        def button_run():
            deck = self.shuffle_cards()
            unpacked_deck = []
            for i in range(len(deck)):
                unpacked_deck.append(deck[i].get_card())
            update_textbox(str(unpacked_deck))

        full_deck = self.get_full_deck()
        print(full_deck)
        window.add_title("Cards", 1, 1)
        entry_button = ttk.Button(window, text="Run algorithm", command=button_run)
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
    cards = Cards(window)