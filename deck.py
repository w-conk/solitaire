import pygame
import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    
    def create_deck(self):
        # Create all 52 cards
        for suit in ["H", "D", "C", "S"]:
            for value in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]:
                self.cards.append(Card(suit, value, f"greywyvern-cardset/{suit}{value}.png"))
        return self.cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None
    
    def get_cards(self):
        return self.cards