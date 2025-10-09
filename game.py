import pygame
from card import Card
from deck import Deck

class SolitaireGame:
    def __init__(self):
        self.deck = Deck()
        self.dragging_card = None
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.card_positions = []
        self.base_x, self.base_y = 100, 100
        for i, card in enumerate(self.deck.cards):
            self.card_positions.append(pygame.Vector2(self.base_x, self.base_y + i * 2))

    def run(self):
        while self.running:
            self.dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill("green")
            for i, card in enumerate(self.deck.cards):
                self.screen.blit(card.get_image(), self.card_positions[i])
            pygame.display.flip()
        # etc.