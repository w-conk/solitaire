import pygame

class Card:
    def __init__(self, suit, value, image_path):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load(image_path)
        self.position = pygame.Vector2(0, 0)
        self.rect = self.image.get_rect()
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value
    
    def get_image(self):
        return self.image
    
    def set_position(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.rect.x = x
        self.rect.y = y

    def get_position(self):
        return self.position