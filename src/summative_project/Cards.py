from tkinter import *
import main

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
suits = ["Diamonds", "Clubs", "Spades", "Hearts"]

class Card:
    def get_card(self):
        return [self.card, self.suit]
    def __init__(self, card, suit):
        if card in cards:
            self.card = card
        if suit in suits:
            self.suit = suit

class Cards:
    def get_full_deck(self):
        deck = []
        for i in cards:
            for j in suits:
                card = Card(i, j)
                deck.append(card.get_card())
                print("deck: " + str(deck))
        return deck

    def __init__(self, window):
        full_deck = self.get_full_deck()
        print(full_deck)
        window.add_title("Cards", 1, 1)

        text_label = Label(window, text="Output (scrollable):")
        text_label.grid(row=3, column=1)
        self.text = Text(window, wrap='word', height=5, width=30)
        self.text.grid(row=4, column=1)
        self.text.config(state="disabled")


def init_window(window):
    window = main.Window("Brute Force", 30, 100)
    window.add_back_button()
    window.parent = window
    cards = Cards(window)